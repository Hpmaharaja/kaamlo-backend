import uuid
import jwt
import json
import time


from passlib.hash import pbkdf2_sha256
import pymysql.cursors

# grab our jwt secret wich will be the word secret for now
jwt_secret = 'secret'

def login_handler(event, context):

    username = event['username']
    password = event['password']

    # connect to the database to fetch login info
    connection = pymysql.connect(
        host="mvp1-kaamlo-logintable.cczywhkujcku.us-west-2.rds.amazonaws.com",
        user="kaamlo",
        password="Radhe108!",
        db="kaamlo",
        charset='utf8mb4',
        port=3306,
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:

            # create a tuple of values to search for in the db
            values = (username, username)

            # retrieve user info
            cursor.execute("""SELECT * FROM `kaamlo_login` where email = %s or username = %s""", values)
            result = cursor.fetchone()

            # pasword validation
            if pbkdf2_sha256.verify(password, result['password']):
                # calculate the expiration time of this token
                expiresAt = time.time() + 3600

                # create the JSON payload to return
                jwt_payload = {
                    'userId': result['user_id'],
                    'exp': expiresAt
                }

                # create the jwt
                jwt_token = jwt.encode(jwt_payload, jwt_secret, algorithm='HS256')

                # return the token
                return {
                    'token': jwt_token,
                    'expiresIn': 3600
                }
            else:
                raise_error(401, "Bad Login")


    except Exception as e:
        return(e)

def raise_error(code, message):
    error = {
        'httpStatus': code,
        'message': message
    }

    raise Exception(json.dumps(error))
