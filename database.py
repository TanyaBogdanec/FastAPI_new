from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine


SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine_db = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_db)

# создаем асинхронный движок
engine = create_async_engine("sqlite+aiosqlite:///tasks.db", echo=True)

# создаем базовый класс для декларативного определения моделей
DeclarativeBase = declarative_base()

# создаем фабрику сессий для асинхронных сессий
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# определение модели
class TaskTable(DeclarativeBase):
    __tablename__ = "tasks"

    # определяем столбец первичного ключа
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)


# функция для создания таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)


# функция для удаления таблиц
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.drop_all)
