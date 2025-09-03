from fastapi import FastAPI
from pydantic import BaseModel
from pyexpat.errors import messages
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def get_pong():
    return Response("pong")

@app.get("/health")
def get_health():
    return Response("Ok" , media_type= "text/plain" , status_code=200)

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    id: str
    brand: str
    model: str
    characteristic: Characteristic

phone_list = [Phone]

def serialized_phone(phone: Phone):
    serialized_phone().append(phone)
    return serialized_phone()

@app.post("/phones")
def get_phones(phone: Phone):
    for phone in phone_list:
        serialized_phone().append(phone)
        return serialized_phone()
    return JSONResponse(status_code=200, content=serialized_phone(), media_type="application/json")

@app.get("/phones")
def get_phone_list(phone: Phone):
    return JSONResponse(status_code=201, content=phone_list , media_type="application/json")

@app.get("/phones/{id}")
def get_phone(id: str):
    for phone in phone_list:
        if phone.id == id:
            return JSONResponse(status_code=200, content=phone.dict(), media_type="application/json")
    return Response(status_code=404, content= "phone not found", media_type="text/plain")

@app.put("/phones/{id}/characteristic")
def update_characteristic(id: str, characteristic: Characteristic):
    for phone in phone_list:
        if phone.id == id:
            phone.characteristic = characteristic
            return JSONResponse(status_code=200, content=phone.dict(), media_type="application/json")
    return Response(status_code=404, content= "phone not found", media_type="text/plain")
