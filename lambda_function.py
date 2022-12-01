import boto3
import json
from boto3.dynamodb.conditions import Key,Attr
def lambda_handler(event, context):
        shahHash = event['params']['path']['shaHash']
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('decrypt')      
        resp = table.query(KeyConditionExpression=Key('key').eq(shahHash))
        print(resp)
        count = resp['Count'] 
        print("Count",count)
        if count == 0: 
          statusCode=404
          password="nil"
          return {'statusCode': statusCode,'body': password}
        else:
          password = resp['Items'][0]
          hash =password['key']
          password = password['value']
          statusCode=200
          return {'statusCode': statusCode,'body': {hash : password}}