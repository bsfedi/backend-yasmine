
import jwt

SECRET_KEY = "M$iY#u$Fn9r=avs$n9$iY#u$F$iY#u$Fn9r=avsn9r=avsn9r=ar=a6n9r=a$iY#u$Fn9Mn9r=amn9r=aOo0n9r=a)#"
JWT_SECRET = "mysecretkey"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 30



def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    # expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    # to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt