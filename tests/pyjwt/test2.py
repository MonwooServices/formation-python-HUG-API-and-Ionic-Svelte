import jwt

data="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVXNlcjIiLCJwYXNzd29yZCI6Ik15cGFzdHdvcmQifQ.Glt1QoSywZ603hsG0YZWrt1O6KQgKAhNF5aXPWzJRkc"

def decode_user(token: str):
    """encoded_data
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(token,
                              'super-secret-key-please-change',
                              algorithms="HS256")

    print(decoded_data)


if __name__ == "__main__":
    try:
        decode_user(data)
        print("ok")
    except:
        print("error")