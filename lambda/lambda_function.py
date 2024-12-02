import json

def lambda_handle(event, context):
    return{
        'statusCode': 200,
        'body': json.dumps('Hello from cicd-test lambda from vscode')
    }