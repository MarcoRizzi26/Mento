from fastapi import FastAPI
from api.routes.main import router as main_router
from api.routes.main import router as api_router

app = FastAPI()

# Incluindo as rotas
app.include_router(main_router)
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
