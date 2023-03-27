from fastapi import FastAPI
from app.user.endpoints import router as userRouter
from app.database import Base,engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Root api"}

app.include_router(userRouter)
Base.metadata.create_all(engine)