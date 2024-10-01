import fastapi
import uvicorn
from api import router

app = fastapi.FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, host='0.0.0.0', port=8000)
