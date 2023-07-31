from peewee import *
from datetime import *
from db_peewee import Message

Message.create(
    date=datetime.today().strftime('%Y-%m-%d'),
    time=datetime.today().strftime('%H:%M:%S'),
    msg="log",
    haveBeenSaid='Hello, i am buddy')
query = Message.select()
for Message in query:
    print(Message.date, Message.time, Message.msg, Message.haveBeenSaid)