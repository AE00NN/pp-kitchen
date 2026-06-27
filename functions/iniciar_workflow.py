import boto3, os, json

sfn = boto3.client('stepfunctions')

def handler(event, context):
    # Llega desde EventBridge cuando Integrante 1 publica order.created
    detail   = event.get('detail', {})
    order_id = detail.get('orderId', 'sin-id')

    sfn.start_execution(
        stateMachineArn=os.environ['STATE_MACHINE_ARN'],
        name=f"orden-{order_id}",
        input=json.dumps({
            'orderId':  order_id,
            'workerId': 'sin-asignar'
        })
    )
    print(f"[iniciar_workflow] Ejecución iniciada para orderId={order_id}")
    return {'ok': True}
