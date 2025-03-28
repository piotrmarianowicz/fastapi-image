from fastapi import FastAPI
from starlette import status
from pydantic import BaseModel, Field

app = FastAPI()

class player():

    def __init__(self, name: str, surname: str, nr: int):
        self.name = name
        self.surname = surname
        self.nr = nr

    name: str
    surname: str
    nr: int

players = [
    player('name1', 'surname1',1),
    player('name2', 'surname2', 2),
    player('name3', 'surname3', 3),
    player('name4', 'surname4', 4),
]

@app.get("/players", status_code=status.HTTP_200_OK)
async def read_root():
    return {"players": players}
