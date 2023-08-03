# TODO : launch backend server...

# python serveur-api 

# Sample from first try :

"""TODO : doc"""
import hug
import jwt
from infrastructure.db_peewee import *
from infrastructure.crypto import *
from datetime import *

@hug.cli()
@hug.local()
@hug.response_middleware()
def CORS(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.set_header(
        'Access-Control-Allow-Headers',
        'Authorization,Keep-Alive,User-Agent,'
        'If-Modified-Since,Cache-Control,Content-Type'
    )
    response.set_header(
        'Access-Control-Expose-Headers',
        'Authorization,Keep-Alive,User-Agent,'
        'If-Modified-Since,Cache-Control,Content-Type'
    )
    if request.method == 'OPTIONS':
        response.set_header('Access-Control-Max-Age', 1728000)
        response.set_header('Content-Type', 'text/plain charset=UTF-8')
        response.set_header('Content-Length', 0)
        response.status_code = hug.HTTP_204

# LIRE les messages de buddy
@hug.get('/api/buddy/read-msgs')
def buddy_api_get():
    """Buddy Have Been Said"""
    return {'buddy-messages': map(lambda m : m.msg, Message.select().where(Message.user == "buddy"))}

# SAUVEGARDE des messages de buddy dans sql
@hug.post('/api/buddy/send-msg')
def buddy_api_post(msg: hug.types.text, hug_timer=3):
    """Buddy Says"""
    create_msg_buddy("Buddy",msg)
    return "buddy message saved"

# SAUVEGARDE des messages de user dans sql
@hug.get('/api/user/send-msg')
def user_api_get(msg: hug.types.text, hug_timer=3):
    """User Says"""
    create_msg_buddy("user",msg)
    return "user_test message saved"


authentication = hug.authentication.basic(hug.authentication.verify('user1', 'password1'))

@hug.authentication.basic
@hug.get('/api/user/token_generation', requires=authentication)  # noqa
def token_gen_call(user: hug.directives.user):
    """Authenticate and return a token"""
    secret_key = getPassword(64)
    update_secretkey(format(user),secret_key)
    print(secret_key)
    return {"user" : format(user), "key": secret_key, "token" : jwt.encode({'user': format(user), "admin": "true"}, secret_key, algorithm='HS256')}


#################################TEST#################################

class APIUser(object):
    """A minimal example of a rich User object"""
    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key



@hug.authentication.api_key
def api_key_verify(api_key):
    magic_key = '5F00832B-DE24-4CAF-9638-C10D1C642C6C'  # Obviously, this would hit your database
    if api_key == magic_key:
        print("succes")
        return APIUser('user_foo', api_key)
    else:
        print("invalid key")
        return None
api_key_authentication = hug.authentication.api_key(api_key_verify)
@hug.get('/key_authenticated', requires=api_key_authentication)  # noqa
def basic_auth_api_call(user: hug.directives.user):
    return 'Successfully authenticated with user: {0}'.format(user.user_id)

###

@hug.authentication.token
def token_verify(token):
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVXNlcjE4IiwiZGF0YSI6Im15ZGF0YSJ9.5OV3BRftmobpMv4BRl1sUyxmUrhj3OJ5PvEMRzYbVYs"
    secret_key = 'super-secret-key-please-change'
    print("token_verify")
    try:
        print("try "+ token)
        a=jwt.decode(token, 'super-secret-key-please-change', algorithms="HS256")
        print(a)
        print("ok")
        return a
    except jwt.DecodeError:
        print("nok")
        return False
token_key_authentication = hug.authentication.token(token_verify)
@hug.get('/token_authenticated', requires=token_key_authentication)  # noqa
def token_auth_call(user: hug.directives.user):
    return 'Successfully authenticated with user: {0}'.format(user.user_id)

############################FIN_TEST#################################

hug.API("api").http.server()

if __name__ == '__main__':
    api.interface.cli()