import jwt
from config import SECRET_KEY, JWT_ALGORITHM

def generate_token(user_id):
    payload = {'user_id': user_id}
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)

def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded['user_id']
    except jwt.InvalidTokenError:
        return None
