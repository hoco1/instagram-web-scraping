import uvicorn
from fastapi import FastAPI,Body,Depends
from app.db import conn
from app.schemas import serializeDict,serializeList
from app.model import InstagramSchema,UserLoginSchema,UserSchema
from app.scraping import *
from bson import ObjectId
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

app = FastAPI()
# Get - for testing
@app.get("/",tags=["test"])
def greet():
    return {"Hello":"World!"}

# All Cookies
@app.get("/cookies",tags=["cookies"])
def get_all_cookies():
    return serializeList(conn.local.cookie.find())

# Single cookie {id}
@app.get("/cookies/{id}",tags=["cookies"])
def get_one_cookie(id:str):
    return serializeDict(conn.local.cookie.find_one({"_id":ObjectId(id)}))

# Get Cookie
@app.post("/cookies",tags=["cookies"])
def add_cookie(instagram:InstagramSchema):
    
    payload = {
    'username': instagram.instagramID,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{instagram.instagramPass}',
    'queryParams': {},
    'optIntoOneTap': 'false'
    }
    login_response = requests.post(login_url, data=payload, headers=login_header)
    cookies = login_response.cookies.get_dict()
    conn.local.cookie.insert_one(dict(cookies))
    return serializeList(conn.local.cookie.find())

# user Signup [Create a new user]
@app.post("/user/signup",tags=["user"])
def user_signup(user:UserSchema=Body(default=None)):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

def check_user(data:UserLoginSchema):
    db_user = conn.local.user.find_one({"email":data.email.lower()})
    
    if not db_user:
        return False
    
    user = serializeDict(db_user)
    
    if not user["password"] == data.password:
        return False
    
    return True
    

@app.post("/user/login",tags=["user"])
def user_login(user:UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"Invalid login details!"
        }
