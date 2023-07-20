# TODO : launch backend server...

# TODO : some __main__.py to be able to easy launch with python ?
# python serveur-api 

# Sample from first try :

"""TODO : doc"""
import hug 
from infrastructure.db_peewee import message

@hug.get(examples='name=Timothy&age=26')
@hug.local()
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Says happy birthday to a user"""

    return {'message': 'Happy {0} Birthday {1}!'.format(age, name),
            'buddy-messages': map(lambda m : m.date, message.select().where(message.haveBeenSaid == 'Hello')),
            'took': float(hug_timer)}

hug.API("api").http.server()