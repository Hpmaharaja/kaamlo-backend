from aws_srp import AWSSRP
import os

def login_handler(event, context):
    username = event['username']
    password = event['password']

    client_id = os.environ['client_id']
    pool_id = os.environ['pool_id']


    try:
        loginClient = AWSSRP(username, password, pool_id, client_id)
        authAttempt = loginClient.authenticate_user()

        return {
            'ExpiresIn': authAttempt['AuthenticationResult']['ExpiresIn'],
            'IdToken': authAttempt['AuthenticationResult']['IdToken']
        }

    except Exception as e:
        print(e)
