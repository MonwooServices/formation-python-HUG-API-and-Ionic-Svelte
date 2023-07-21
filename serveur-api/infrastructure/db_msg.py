from peewee import *
from datetime import *
from db_peewee import message

message.create(
    date=datetime.today().strftime('%Y-%m-%d'),
    time=datetime.today().strftime('%H:%M:%S'),
    msg="log",
    haveBeenSaid='Hello, i am buddy')
query = message.select()
for message in query:
    print(message.date, message.time, message.msg, message.haveBeenSaid)