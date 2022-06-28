import boto3
import simplejson as json
import os
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('CUSTOMERS_TABLE')

def lambda_handler(event,context):
    table = dynamodb.Table(table_name)
    customer_id = int(event['pathParameters']['id'])
    response = table.query(KeyConditionExpression=Key('id').eq(customer_id))
    print(response)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }