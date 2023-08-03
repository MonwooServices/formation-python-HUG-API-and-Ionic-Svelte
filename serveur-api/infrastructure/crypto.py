from uuid import uuid4
import string, random
 
def getPassword(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    #str = string.ascii_lowercase
    str = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(str) for i in range(length))

def getToken():
    token = uuid4()
    return token
