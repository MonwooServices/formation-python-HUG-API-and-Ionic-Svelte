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

@hug.get('/headers', output=hug.output_format.json)
def headers(request, header_name: hug.types.text=None):
    if header_name is None:
        return request.headers
    return {header_name: request.get_header(header_name)}

hug.API("api").http.server()

if __name__ == '__main__':
    api.interface.cli()