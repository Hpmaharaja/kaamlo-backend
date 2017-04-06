import boto3
import uuid
import json

def register_handler(event, context):
    client = boto3.client('cognito-idp')

    try:
        response = client.sign_up(
            ClientId = '1uev7o0p0qhj8lp52mcj2lt2hp',
            Username = event['username'],
            Password = event['password'],
            UserAttributes = [
                {
                    'Name': 'email',
                    'Value': event['email']
                },
                {
                    'Name': 'family_name',
                    'Value': event['lastName']
                },
                {
                    'Name': 'name',
                    'Value': event['firstName']
                }
            ]
        )
    except Exception as e:

        errorResponse = e.response['Error']
        error = {
            'status': errorResponse['Code'],
            'httpStatus': 400,
            'message': errorResponse['Message']
        }

        raise Exception(json.dumps(error))

    registered = response['UserConfirmed']
    return {
        'status': 'ok',
        'code': 200,
        'registered': registered
    }
