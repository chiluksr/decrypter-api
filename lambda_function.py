import json
import boto3

def lambda_handler(event, context):
    responseflag = 0
    hash_key=event['path'][1:]
    s3_connect=boto3.client("s3")
    response=s3_connect.select_object_content(
        Bucket='decrypterservice',
        Key='output.csv',
        ExpressionType='SQL',
        Expression=f"Select s.password From s3object s where s.shaHash='{hash_key}'",
        InputSerialization={'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
        OutputSerialization={'CSV': {}},
    )
    print(response)
    for event in response['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            responseflag=1
            print(records)
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            print(statsDetails['BytesScanned'])
            print("Stats details bytesProcessed: ")
            print(statsDetails['BytesProcessed'])
            print("Stats details bytesReturned: ")
            print(statsDetails['BytesReturned'])
    
    if responseflag == 1 :
        s=records.rstrip()
        return {
            'statusCode': 200,
            'body': json.dumps({hash_key:s})
        }
    else :
        return {
            'statusCode': 404,
            'body': ""
        }
        
