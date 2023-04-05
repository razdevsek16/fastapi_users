from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.user.endpoints import router as userRouter
from app.auth.endpoints import router as authRouter
from app.track.endpoints import router as trackRouter
from app.database import Base,engine


Base.metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(userRouter)
app.include_router(authRouter)
app.include_router(trackRouter)

@app.get("/")
async def root():
    return {"message":"Root api"}