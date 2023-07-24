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

hug.API("api").http.server()

if __name__ == '__main__':
    api.interface.cli()