# TODO : launch backend server...

# python serveur-api 

# Sample from first try :

"""TODO : doc"""
import hug
import jwt
from infrastructure.db_peewee import Message

@hug.cli()
#@hug.get(examples='msg=log&date=2023-07-21')
@hug.local()

@hug.get('/api/buddy/read-msgs')
def buddy_api_call():
    """Buddy Says"""

    return {'buddy-messages': map(lambda m : m.msg, Message.select())}


# POST pour budy messages
@hug.post('/api/buddy/send-msg')
def buddy_api_post(msg: hug.types.text, hug_timer=3):
    """Buddy Says"""

    return "test post ok"


authentication = hug.authentication.basic(hug.authentication.verify('User12', 'mypastword'))


@hug.get('/public')
def public_api_call():
    return "Needs no authentication"


# Note that the logged in user can be accessed via a built-in directive.
# Directives can provide computed input parameters via an abstraction
# layer so as not to clutter your API functions with access to the raw
# request object.
@hug.get('/authenticated', requires=authentication)
def basic_auth_api_call(user: hug.directives.user):
    return 'Successfully authenticated with user: {0}'.format(user)


# Here is a slightly less trivial example of how authentication might
# look in an API that uses keys.

# First, the user object stored in the context need not be a string,
# but can be any Python object.
user_id="1234"
class APIUser(object):
    """A minimal example of a rich User object"""

    def __init__(user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key


def api_key_verify(api_key):
    api_key = '5F00832B-DE24-4CAF-9638-C10D1C642C6C'  # Obviously, this would hit your database
    if api_key == '5F00832B-DE24-4CAF-9638-C10D1C642C6C':
        print("succes")
        # Success!
        return APIUser('user_foo', api_key)
    else:
        print("invalid key")
        # Invalid key
        return None


api_key_authentication = hug.authentication.api_key(api_key_verify)


@hug.get('/key_authenticated', requires=api_key_authentication)  # noqa
def basic_auth_api_call(user: hug.directives.user):
    return 'Successfully authenticated with user: {0}'.format(user_id)


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


token_key_authentication = hug.authentication.token(token_verify("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVXNlcjE4IiwiZGF0YSI6Im15ZGF0YSJ9.5OV3BRftmobpMv4BRl1sUyxmUrhj3OJ5PvEMRzYbVYs"))


@hug.get('/token_authenticated', requires=token_key_authentication)  # noqa
def token_auth_call(user: hug.directives.user):
    return 'Successfully authenticated with user: {0}'.format(user_id)


@hug.get('/token_generation')  # noqa
def token_gen_call(username, pastword):
    print("token")
    """Authenticate and return a token"""
    secret_key = 'super-secret-key-please-change'
    mockusername = 'User18'
    mockpastword = 'Mypastword'
    if mockpastword == pastword and mockusername == username: # This is an example. Don't do that.
        print("ok")
        return {"token" : jwt.encode({'user': username, 'data': 'mydata'}, 'super-secret-key-please-change', algorithm='HS256')}
    else:
        return 'Invalid username and/or pastword for user'

@hug.get('/hello', requires=api_key_authentication)
def hello_world():
    return 'Hello world!'

@hug.post(examples='msg=log&date=2023-07-21')
@hug.local()
def update_user(name: hug.types.text):
    return {"message" : f"the salary {name}"}


@hug.directive()
def basic(default=False, **kwargs):
    return str(default) + ' there!'

@hug.local()
def endpoint(hug_basic='hi'):
    return hug_basic
assert endpoint() == 'hi there!'

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


hug.API("api").http.server()

if __name__ == '__main__':
    api.interface.cli()