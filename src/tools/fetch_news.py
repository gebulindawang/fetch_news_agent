import httpx

def search_news(platform:str) ->dict:
    result = httpx.get("https://news.orz.ai/api/v1/dailynews/",params={"platform":"juejin"})
    news = result.json()
    articles = news["data"]
    return articles

