from fastapi import FastAPI
from .routes.events import event_router
from .routes.users import user_router

app = FastAPI()

app.include_router(event_router)
app.include_router(user_router)

@app.get("/")
async def root_path():
    return "Hello World!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "mian.app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )