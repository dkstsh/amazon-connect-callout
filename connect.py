import boto3

client = boto3.client('connect')

response = client.start_outbound_voice_contact(
    DestinationPhoneNumber='replace-with-number-you-want-call-out',
    ContactFlowId='replace-with-your-ContactFlowId',
    InstanceId='replace-with-your-InstanceId',
    SourcePhoneNumber='replace-with-your-SourcePhoneNumber',
    Attributes={
        'name': 'alert'
    }
)

print response