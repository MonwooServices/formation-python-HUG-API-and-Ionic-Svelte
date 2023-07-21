from peewee import *

db = SqliteDatabase('buddy-api.db.sqlite')

class message(Model):
    date = DateField()
    time = DateField()
    msg = CharField()
    haveBeenSaid = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([message])