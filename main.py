from fastapi import FastAPI, APIRouter

app = FastAPI()

# 创建 subscriptions 路由组
router = APIRouter(prefix="/subscriptions")


@router.get("/health")
async def health_check():
    return {"status": "ok"}


app.include_router(router)


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
