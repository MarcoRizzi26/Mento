from queue import Queue

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from modules.api.routes.main import router as api_router
from modules.api.shared import SharedQueue

app = FastAPI()

# origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(api_router)

def start_api(queue: Queue):
    print("Running on port 3000")
    SharedQueue.QUEUE = queue
    uvicorn.run(app=app, host='0.0.0.0', port=3000, log_level="info")