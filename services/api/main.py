from fastapi import FastAPI
from .endpoints import public_data

app = FastAPI()

app.include_router(public_data.router, prefix="/public", tags=["public"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Coinbase Public Data API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
