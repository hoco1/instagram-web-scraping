from pydantic import BaseModel,Field,EmailStr

class InstagramSchema(BaseModel):
    instagramID:str = Field(default=None)
    instagramPass:str = Field(default=None)
    class Config:
        schema_extra={
            "Instagram_demo":{
                "instagramID":"id",
                "instagramPass":"####"
            }
        }

class UserSchema(BaseModel):
    fullname:str=Field(default=None)
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "name":"norouzi",
                "email":"norouzi_reza78@yahoo.com",
                "password":"123"
            }       
        }
        
class UserLoginSchema(BaseModel):
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "email":"norouzi_reza78@yahoo.com",
                "password":"123"
            } 
        }