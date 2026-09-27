from typing import TypedDict,Annotated
from pydantic import BaseModel
from datetime import datetime
class article(BaseModel):
    id: int
    titile:str
    content:str
    url:str
    author:str
    platform:str


class NewsState (TypedDict):
    id : int 
    articles:list
    start_time:datetime
    end_time:datetime
    user_input :str
    analyze:str
    

