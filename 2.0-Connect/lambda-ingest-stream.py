import json
import boto3


def lambda_handler(event, context):

    print(f'Event: {event}')

    method = event['context']['http-method']
    if method == 'POST':
        ec_record = event['body-json']
        ec_record_str = json.dumps(ec_record)

        client = boto3.client('kinesis')
        
