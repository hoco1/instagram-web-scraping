import uvicorn
from fastapi import FastAPI
from app.db import conn
from app.schemas import serializeDict,serializeList
from app.model import InstagramSchema
from app.scraping import *
from bson import ObjectId

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