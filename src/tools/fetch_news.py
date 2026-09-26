import httpx
import time

result = httpx.get("https://news.orz.ai/api/v1/dailynews/",params={"platform":"juejin"})
news = result.json()
articles = news["data"]

for article in articles:
    time.sleep(3)
    print(article)

