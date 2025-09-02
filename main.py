from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get("/ping")
def get_pong():
    return Response("pong")