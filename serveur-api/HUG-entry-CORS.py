# TODO : launch backend server...

# python serveur-api 

# Sample from first try :

"""TODO : doc"""
import hug 
from infrastructure.db_peewee import message

@hug.cli()
@hug.get(examples='msg=log&date=2023-07-21')
@hug.local()

def api(msg: hug.types.text, date: hug.types.text, hug_timer=3):
    """Buddy Says"""

    return {'msg': '{0}'.format(msg),
            'buddy-messages': map(lambda m : m.haveBeenSaid, message.select().where(message.msg == msg, message.date == date)),
            'took': float(hug_timer)}

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