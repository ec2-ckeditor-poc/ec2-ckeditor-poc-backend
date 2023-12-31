import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # DynamoDB table name
    table_name = 'VisitorCounter'
    
    # Create a DynamoDB client using boto3
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Increment the visitor count
    try:
        response = table.update_item(
            Key={'id': 1},
            UpdateExpression="SET visitor_count = if_not_exists(visitor_count, :start) + :inc",
            ExpressionAttributeValues={':start': 0, ':inc': 1},
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        new_visitor_count = response['Attributes']['visitor_count']
        print(f'New visitor count (pipeline commit): {new_visitor_count}')
        return {
            'statusCode': 200,
            'body': json.dumps({'visitor_count': int(new_visitor_count)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }