from fastapi import FastAPI, HTTPException, status
from src.users.router import router as users_router

app = FastAPI()
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

