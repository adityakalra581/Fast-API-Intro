## FastAPI-login 
## https://pypi.org/project/fastapi-login/

from fastapi import FastAPI
from fastapi_login import LoginManager
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException


app = FastAPI()

SECRET_KEY = "thisisasecret"


manager = LoginManager(SECRET_KEY, tokenUrl='/auth/token')

fake_db = {'johndoe@e.mail': {'password': 'hunter2'}}

@manager.user_loader
def load_user(email: str):  # could also be an asynchronous function
    user = fake_db.get(email)
    return user


@app.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = load_user(email)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=email)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}