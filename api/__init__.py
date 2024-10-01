import fastapi

from api.breeds.view import router as breeds_router
from api.cats.view import router as cats_router

router = fastapi.APIRouter(prefix='')

router.include_router(cats_router)
router.include_router(breeds_router)
