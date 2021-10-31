from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import wordcount as wc


app = FastAPI()


class Site(BaseModel):
    url: str


@app.get("/")
def root():
    return {"message": "That's wordcount!"}


@app.post("/wordcount/")
async def post_wordcount(site: Site):
    wp_text = wc.get_html_from_url(site.url)
    cl_list = wc.create_words_list(wp_text)
    return wc.wordcount(cl_list)

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="info")