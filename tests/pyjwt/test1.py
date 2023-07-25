import jwt

def encode_user():
    """
    encode user payload as a jwt
    :param user:
    :return:
    """
    encoded_data = jwt.encode(payload={"name": "Buddy"},
                              key='mon_password_secret',
                              algorithm="HS256")
    #print(encoded_data)
    return encoded_data

def decode_user(token: str):
    """encoded_data
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token,
                              key='mon_password_secret',
                              algorithms="HS256")

    print(decoded_data)


if __name__ == "__main__":
    data=encode_user()
    try:
        decode_user(data)
        print("ok")
    except:
        print("error")