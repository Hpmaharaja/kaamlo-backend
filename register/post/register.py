import uuid
import jwt
import json
import time

from passlib.hash import pbkdf2_sha256
import pymysql.cursors

# grab our jwt secret wich will be the word secret for now
jwt_secret = 'secret'

def register_handler(event, context):

    # invoke a mysql connection and attempt to add it
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
        # load the data from the post request
        username = event['username']
        password = event['password']
        first_name = event['firstName']
        last_name = event['lastName']
        email = event['email']

        #generate a unique user_id for the user
        user_id = str(uuid.uuid4())

        # hash the user's password
        hashed_password = pbkdf2_sha256.hash(password)

        with connection.cursor() as cursor:

            # create a tuple of values to insert in to the database
            values = (user_id, username, hashed_password, email, first_name, last_name)

            # insert into the database
            cursor.execute("""INSERT INTO `kaamlo_login` (`user_id`, `username`, `password`, `email`, `first_name`, `last_name`, `verified`)
            VALUES (%s, %s, %s, %s, %s, %s, 0)""", values)

        connection.commit()

        # calculate the expiration time of this token
        expiresAt = time.time() + 3600

        # create the JSON payload to return
        jwt_payload = {
            'userId': user_id,
            'exp': expiresAt
        }

        # create the jwt
        jwt_token = jwt.encode(jwt_payload, jwt_secret, algorithm='HS256')

        # return the token
        return {
            'token': jwt_token,
            'expiresIn': 3600
        }

    except Exception as e:
        if "Duplicate" in str(e):
            raise_error(400, "User already exists")
        else:
            raise_error(500, "Interal Server Error")

    finally:
        connection.close()

def raise_error(code, message):
    error = {
        'httpStatus': code,
        'message': message
    }

    raise Exception(json.dumps(error))
