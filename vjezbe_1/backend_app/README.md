# Backend – Blog REST API (FastAPI)

**URL:** https://miniblog-vdadic-api.onrender.com
**Dokumentacija:** https://miniblog-vdadic-api.onrender.com/docs

## Endpointi

| Metoda | Putanja | Opis |
|---|---|---|
| GET | / | provjera rada servera |
| GET | /posts | sve objave |
| GET | /posts/{id} | jedna objava |
| POST | /posts | nova objava (JSON: title, content) |
| DELETE | /posts/{id} | brisanje objave |