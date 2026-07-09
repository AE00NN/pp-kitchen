import boto3, os
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TASKS_TABLE'])

def handler(event, context):
    table.put_item(Item={
        'orderId':   event['orderId'],
        'estado':    event['estado'],
        'tenantId':  event.get('tenantId', 'sin-tenant'),
        'workerId':  event.get('workerId', 'sin-asignar'),
        'taskToken': event['taskToken'],
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'completado': False
    })
    print(f"[registrar] {event['orderId']} → {event['estado']}")
    return {'ok': True}
