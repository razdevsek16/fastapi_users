from fastapi import FastAPI
from app.user.endpoints import router as userRouter
from app.auth.endpoints import router as authRouter
from app.database import Base,engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Root api"}

app.include_router(userRouter)
app.include_router(authRouter)
Base.metadata.create_all(engine)