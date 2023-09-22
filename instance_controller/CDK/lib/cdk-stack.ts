import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { CloudFrontToS3 } from '@aws-solutions-constructs/aws-cloudfront-s3';
const path = require('path');

export class CdkStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        new CloudFrontToS3(this, 'instance-controller-website-bucket', {});

        //python lambda funtion with a function url
        const lambda = new cdk.aws_lambda.Function(this, 'python-function', {
            code: cdk.aws_lambda.Code.fromAsset(
                path.join(__dirname, '../lambda')
            ),
            handler: 'lambda_handler',
            runtime: cdk.aws_lambda.Runtime.PYTHON_3_11,
        });

        lambda.addFunctionUrl();

        const pool = new cdk.aws_cognito.UserPool(this, 'Pool');
        pool.addClient('app-client', {
            oAuth: {
                flows: {
                    authorizationCodeGrant: true,
                },
                scopes: [cdk.aws_cognito.OAuthScope.OPENID],
                callbackUrls: [
                    'https://d3ldmqb2ua8wew.cloudfront.net/welcome',
                    'https://d3ldmqb2ua8wew.cloudfront.net/',
                ],
                logoutUrls: [
                    'https://d3ldmqb2ua8wew.cloudfront.net/signin',
                    'https://d3ldmqb2ua8wew.cloudfront.net/',
                ],
            },
        });
    }
}
