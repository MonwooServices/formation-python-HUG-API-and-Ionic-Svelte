from peewee import *
from datetime import *

# This is the database repertory
db_rep = "serveur-api/infrastructure/database/"

# This model uses the "buddy-api.db.sqlite" database
db_buddy = SqliteDatabase(db_rep +'buddy-api.db.sqlite')
class Message(Model):
    date = DateField()
    time = DateField()
    msg = CharField()
    class Meta:
        database = db_buddy

# This model uses the "user-api.db.sqlite" database
db_user = SqliteDatabase(db_rep +'user-api.db.sqlite')
class User(Model):
    identity = CharField()
    name = CharField()
    password = CharField()
    key = CharField()
    class Meta:
        database = db_user

# Creating table "Message" in "buddy-api.db.sqlite" database
def create_table_msg_buddy():
    db_buddy.connect()
    db_buddy.create_tables([Message])
    db_buddy.close()

# Creating data in table "Message"
def create_msg_buddy(var_msg):
    Message.create(
        date=datetime.today().strftime('%Y-%m-%d'),
        time=datetime.today().strftime('%H:%M:%S'),
        msg=var_msg
        )

# Creating table "User" in "user-api.db.sqlite" database
def create_table_user_buddy():
    db_user.connect()
    db_user.create_tables([User])
    db_user.close()

# Creating data in table "User"
def create_user_buddy(var_name):
    User.create(
        identity="ec6a3dae-0278-49d5-b909-03846369bae4",
        name=var_name,
        password="1234",
        key="HWeC6Tp4hTxXGPStfJgjoirj3XdzPgfBuf6CbRf8xF3Iacz4f7di1taQf6a05tlR="
        )

### Commands test ###

#create_table_msg_buddy()
#create_table_user_buddy()
#create_msg_buddy("buddy")
#create_user_buddy("nicolas")