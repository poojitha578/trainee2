
from controller.controller import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

@app.get("/")
def get():
    return{
        "msg":"hello to all.... welcome to RCV"
    }

