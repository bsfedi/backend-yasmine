from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from user.router import user_router

app = FastAPI()


app.include_router(user_router)

""" allows a server to indicate any origins (domain, scheme, or port) """
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=5000, reload=True)