from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
_db: Dict[str, str] = {}

class Person(BaseModel):
    name: str
    country: str

@app.get("/greet")
def greet():
    """Return a simple greeting."""
    return {"message": "¡Hola desde la API!"}

@app.post("/info")
def set_info(person: Person):
    """Store name and country in memory."""
    _db[person.name] = person.country
    return {"status": "ok", "name": person.name, "country": person.country}

@app.get("/country/{name}")
def get_country(name: str):
    """Return stored country for a given name."""
    if name not in _db:
        raise HTTPException(status_code=404, detail="Not found")
    return {"name": name, "country": _db[name]}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("src.api.main:app", host="127.0.0.0", port=8001, reload=True)
