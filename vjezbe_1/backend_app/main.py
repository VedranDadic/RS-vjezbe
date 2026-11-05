from datetime import date

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Blog API")

# CORS - dopušta frontendu s druge adrese da šalje zahtjeve ovom serveru
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Oblik podataka koji klijent šalje kad stvara novu objavu
class NewPost(BaseModel):
    title: str
    content: str


# Baza podataka je lista u memoriji - restart servera znači da se sve briše!
posts = [
    {
        "id": 1,
        "title": "Prva objava",
        "date": "2026-11-05",
        "content": "Najoriginalnija ideja za projekt ikad.",
    },

]
next_id = 2


@app.get("/")
def root():
    return {"message": "Miniblog API ok"}


@app.get("/posts")
def get_posts():
    return posts


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Objava nije pronađena")


@app.post("/posts", status_code=201)
def create_post(new_post: NewPost):
    global next_id
    post = {
        "id": next_id,
        "title": new_post.title,
        "date": str(date.today()),
        "content": new_post.content,
    }
    posts.append(post)
    next_id += 1
    return post


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            return {"message": "Objava obrisana"}
    raise HTTPException(status_code=404, detail="Objava nije pronađena")