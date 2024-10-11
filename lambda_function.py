import json
import boto3
from botocore.exceptions import ClientError

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyTable')  # Replace with your table name

def lambda_handler(event, context):
    # Extract primary key value from the query parameters or request body
    try:
        if 'queryStringParameters' in event and event['queryStringParameters']:
            primary_key_value = event['queryStringParameters'].get('pri_key')
        else:
            body = json.loads(event.get('body', '{}'))
            primary_key_value = body.get('pri_key')

        if not primary_key_value:
            raise ValueError("Primary key value is required")

        # Fetch the item from DynamoDB
        response = table.get_item(Key={'pri_key': primary_key_value})
        item = response.get('Item', {})

        if not item:
            raise Exception("Item not found")

        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": str(e)})
        }
