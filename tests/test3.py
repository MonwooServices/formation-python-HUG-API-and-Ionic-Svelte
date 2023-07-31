from uuid import uuid4
import string, random
 
rand = random.choice(string.ascii_letters)
print(rand)

def getPassword(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    #str = string.ascii_lowercase
    str = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(str) for i in range(length))
    
print (getPassword(64)+"=" )

rand_token = uuid4()
print(rand_token)