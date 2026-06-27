import boto3, os, json
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
sfn      = boto3.client('stepfunctions')
table    = dynamodb.Table(os.environ['TASKS_TABLE'])

def handler(event, context):
    body     = json.loads(event.get('body', '{}'))
    order_id = body['orderId']
    estado   = body['estado']

    item = table.get_item(Key={'orderId': order_id, 'estado': estado}).get('Item')
    if not item:
        return _resp(404, {'error': f'No existe tarea {order_id} / {estado}'})
    if item.get('completado'):
        return _resp(400, {'error': 'Paso ya completado'})

    sfn.send_task_success(
        taskToken=item['taskToken'],
        output=json.dumps({'orderId': order_id, 'estadoCompletado': estado})
    )
    table.update_item(
        Key={'orderId': order_id, 'estado': estado},
        UpdateExpression='SET completado = :v, completado_en = :t',
        ExpressionAttributeValues={':v': True, ':t': datetime.now(timezone.utc).isoformat()}
    )
    print(f"[completar] {order_id} → {estado} OK")
    return _resp(200, {'ok': True})

def _resp(status, body):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(body)
    }
