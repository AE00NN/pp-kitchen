import boto3, os, json
from datetime import datetime, timezone

events    = boto3.client('events')
EVENT_BUS = os.environ['EVENT_BUS_NAME']

def handler(event, context):
    events.put_events(Entries=[{
        'Source':       'pp.kitchen',
        'DetailType':   'step.completed',
        'EventBusName': EVENT_BUS,
        'Detail': json.dumps({
            'orderId':   event['orderId'],
            'tenantId':  event.get('tenantId', 'default'),
            'estado':    event['estado'],
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'origin':    'pp-kitchen'
        })
    }])
    print(f"[emitir] step.completed {event['orderId']} → {event['estado']}")
    return {'ok': True}
