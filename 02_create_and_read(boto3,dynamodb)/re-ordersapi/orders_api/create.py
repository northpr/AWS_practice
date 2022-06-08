import boto3
import simplejson as json
import os

dynamodb = boto3.resource('dynamodb')  # access dynamodb resource
table_name = os.environ.get('ORDERS_TABLE')  # from the environment available


def lambda_handler(event,context):
    order = json.loads(event['body'])
    table = dynamodb.Table(table_name) # fetching the table_name
    response = table.put_item(TableName=table_name, Item=order)
    print(response)

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message':'Order Created'})
    }