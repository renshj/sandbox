import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

def parse_event(event):
    action = 'INVALID_ACTION'
    instance_id = 'INVALID_INSTANCE'
    resp = [action, instance_id]

    if event.contains('start'):
        action = 'ON'
    elif event.contains('stop'):
        action = 'OFF'

    if event.contains('instance_id'):
        instance_id = event['instance_id']

    return resp

def lambda_handler(event, context):
    resp = ''
    action, instance_id = parse_event(event)

    if action == 'ON':
        # Do a dryrun first to verify permissions
        try:
            ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, run start_instances without dryrun
        try:
            response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)
            return {
                'body': e,
                'statusCode': '400',
            }
    else:
        # Do a dryrun first to verify permissions
        try:
            ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, call stop_instances without dryrun
        try:
            response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)
            return {
                'body': e,
                'statusCode': '400',
            }

    return {
        'body': resp,
        'statusCode': '200',
    }