from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def check_status():
    return {"message": "Without sacrifice, there is no victory"}