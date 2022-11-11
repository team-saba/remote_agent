from fastapi import FastAPI
from routers.router import api_router

app = FastAPI(
    title='Saba Remote Agent API',
    description='BoB11기 프로젝트 Saba의 Remote Agent API 서버입니다.',
    version='0.1.0',
)

app.include_router(api_router)

@app.get("/7qy38tiejfkdnojiwgu9eyhijdfk")
def server_checker():
    return {"Hello": "World"}