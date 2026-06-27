import boto3, os, json
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table(os.environ['TASKS_TABLE'])

def handler(event, context):
    # Escanea tareas no completadas (cola FIFO por timestamp)
    result = table.scan(
        FilterExpression=Attr('completado').eq(False)
    )
    tareas = sorted(result.get('Items', []), key=lambda x: x.get('timestamp', ''))
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'tareas': tareas}, default=str)
    }
