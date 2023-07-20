from peewee import *
from datetime import date

db = SqliteDatabase('buddy-api.db.sqlite.test')

class message(Model):
    date = DateField()
    haveBeenSaid = CharField()
    msg = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()

query = message.select().where(message.haveBeenSaid == 'Hello')
for message in query:
    print(message.msg)
#print(query)