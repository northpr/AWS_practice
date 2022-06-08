import boto3
import simplejson as json
import os


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('CUSTOMERS_TABLE')
    customer = json.loads(event['body'])
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=customer)
    print(response)

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Customer Created'})
    }
