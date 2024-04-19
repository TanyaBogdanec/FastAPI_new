from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


# декоратор, который помогает создавать контекстные менеджеры
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # удаление таблицы
        await delete_tables()
        print("Base clean")
        # создание таблицы
        await create_tables()
        print("Base ready to go")
        yield
    finally:
        # закрытие таблицы
        print("Base close")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

