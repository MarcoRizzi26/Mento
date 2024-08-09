from fastapi import FastAPI
from api.routes import main as main_routes
from api.routes.main import router as api_router

app = FastAPI()

app.include_router(main_routes.router)
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
