from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    likes: int

    class Config:
        orm_mode = True

class PostComment(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True


class Comment(BaseModel):
    comment: str
    created_at: datetime

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    comment: str
    published: bool= True

class CommentOut(BaseModel):
    Post: PostComment
    Comment: Comment
    likes: int
    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

