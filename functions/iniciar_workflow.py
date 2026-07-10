import boto3, os, json

sfn = boto3.client('stepfunctions')

def handler(event, context):
    detail   = event.get('detail', {})
    order_id = detail.get('orderId', 'sin-id')
    tenant_id = detail.get('tenantId', 'popeyes')

    sfn.start_execution(
        stateMachineArn=os.environ['STATE_MACHINE_ARN'],
        name=f"orden-{order_id}",
        input=json.dumps({
            'orderId':  order_id,
            'tenantId': tenant_id,
            'workerId': 'sin-asignar'
        })
    )
    print(f"[iniciar_workflow] orderId={order_id} tenantId={tenant_id}")
    return {'ok': True}
