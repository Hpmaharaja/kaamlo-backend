import os
import requests
import facebook
import boto3

def facebook_callback(event, context):
    code = event['code']

    fb_client = os.environ['fb_client']
    fb_secret = os.environ['fb_secret']
    redirect_uri = os.environ['redirect_uri']
    pool_id = os.environ['pool_id']

    payload = {
    'client_id': fb_client,
    'redirect_uri': redirect_uri,
    'client_secret': fb_secret,
    'code': code
    }

    try:
        r = requests.get('https://graph.facebook.com/v2.8/oauth/access_token', payload)
        response = r.json()

        access_token = response['access_token']

        graph = facebook.GraphAPI(access_token= access_token)
        args = {'fields' : 'id,email,first_name, last_name'}
        profile = graph.get_object('me', **args)
        return(profile)
    except Exception as e:
        print(e)

def user_exists(email):
        
