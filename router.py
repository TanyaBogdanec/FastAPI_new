from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Taski"]
)


# отправка данных
@router.post("", status_code=201)
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    try:
        task_id = await TaskRepository.add_one(task)
        return {"ok": True, "task_id": task_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


# получение данных
@router.get("")
async def get_tasks() -> list[STask]:
    try:
        tasks = await TaskRepository.find_all()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
