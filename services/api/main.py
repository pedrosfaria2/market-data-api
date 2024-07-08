from fastapi import FastAPI
from .endpoints import public_data  # Import the router from the public_data module

# Create an instance of the FastAPI application
app = FastAPI()

# Include the router for public data endpoints with a prefix and tag
app.include_router(public_data.router, prefix="/public", tags=["public"])

# Define the root endpoint of the application
@app.get("/")
def read_root():
    """
    Root endpoint of the API.
    
    Returns:
        dict: A welcome message for the API.
    """
    return {"message": "Welcome to the Coinbase Public Data API"}

# Entry point for running the application
if __name__ == "__main__":
    import uvicorn  # Import uvicorn for running the application

    # Run the FastAPI application with Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=8000)
