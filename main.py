from datetime import datetime
from typing import Union

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify the exact origins ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return {
    "message": "핼로 월드!",
    "current_time": "2024-06-13 12:34:56"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")