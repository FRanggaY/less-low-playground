from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router as api_router

# whitelist alloed routes
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
]

app = FastAPI(
    title="Less Low Playground"
)

# cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def check_status():
    return {"message": "Without sacrifice, there is no victory"}


# Include the API router
app.include_router(api_router, prefix="/api/v1")