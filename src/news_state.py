from typing import TypedDict,Annotated
from pydantic import BaseModel
from datetime import datetime

class NewsState (TypedDict):
    id : int 
    articles:list
    start_time:datetime
    end_time:datetime
    user_input :str
    analyze:str

class ArticleSchema(BaseModel):
    title:Annotated[str, "文章标题"]
    url:Annotated[str, "文章链接"]
    summary:Annotated[str, "文章摘要"]
    reason:Annotated[str, "推荐理由"]

class AnalyzeResult(BaseModel):
    analyze:Annotated[list[ArticleSchema], "分析结果"]
    

