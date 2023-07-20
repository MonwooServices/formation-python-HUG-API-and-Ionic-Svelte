from peewee import *
from datetime import *

db = SqliteDatabase('buddy-api.db.dev.sqlite')

class message(Model):
    date = DateField()
    time = DateField()
    haveBeenSaid = CharField()
    msg = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([message])
message.create(
    date=datetime.today().strftime('%Y-%m-%d'),
    time=datetime.today().strftime('%H:%M:%S'),
    haveBeenSaid='Hello',
    msg='ok')
query = message.select().where(message.haveBeenSaid == 'Hello')
for message in query:
    print(message.date, message.time)