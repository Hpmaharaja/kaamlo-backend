import os
import requests
import facebook
import pymysql
import time
import jwt
import uuid
import json

def facebook_callback(event, context):
    code = event['code']

    fb_client = os.environ['fb_client']
    fb_secret = os.environ['fb_secret']
    redirect_uri = os.environ['redirect_uri']

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

        connection = pymysql.connect(
            host="mvp1-kaamlo-logintable.cczywhkujcku.us-west-2.rds.amazonaws.com",
            user="kaamlo",
            password="Radhe108!",
            db="kaamlo",
            charset='utf8mb4',
            port=3306,
            connect_timeout=5,
            cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # create a tuple of values to search for in the db
            values = (profile['email'])

            # retrieve user info
            cursor.execute("""SELECT * FROM `kaamlo_login` where email = %s""", values)
            result = cursor.fetchone()

            if result is None:
                # register the user

                # create a dummy password for the user
                password = str(uuid.uuid4())

                payload = {
                    'username': profile['email'],
                    'email': profile['email'],
                    'password': password,
                    'firstName': profile["first_name"],
                    'lastName': profile["last_name"]
                }

                r = requests.post('https://s02hzb0be3.execute-api.us-west-2.amazonaws.com/beta1/register',
                    data = json.dumps(payload))

                if r.status_code != 200:
                    raise Exception('http://localhost:8080')
                else:
                    response = r.json()
                    raise Exception('http://localhost:8080?auth=' + response['token'])

                return(r)



            else:
                # login the user

                # calculate the expiration time of this token
                expiresAt = time.time() + 3600

                # create the JSON payload to return
                jwt_payload = {
                    'userId': result['user_id'],
                    'exp': expiresAt
                }

                # create the jwt
                jwt_token = jwt.encode(jwt_payload, 'secret', algorithm='HS256')

                # return the token
                raise Exception('http://localhost:8080/fb-login/' + jwt_token)


    except Exception as e:
        raise raise Exception('http://localhost:8080/login?q=login_error')

def raise_error(code, message):
    error = {
        'httpStatus': code,
        'message': message
    }

    raise Exception(json.dumps(error))
