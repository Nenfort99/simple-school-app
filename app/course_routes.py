
from app.models import Course, CourseIn_Pydantic, Course_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


course_router = APIRouter()


class Message(BaseModel):
    message: str
# Defining a simple Pydantic model for response messages (used in the delete operation), with a single field `message`.

@course_router.get('/api/courses', response_model=List[Course_Pydantic])
async def get_all_courses():
    return await Course_Pydantic.from_queryset(Course.all())

@course_router.post('/api/course', response_model=Course_Pydantic)
async def create_a_course(course: CourseIn_Pydantic):
    courseobj = await Course.create(**course.dict(exclude_unset=True))
    return await Course_Pydantic.from_tortoise_orm(courseobj)

@course_router.get('/api/course/{id}', response_model=Course_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_a_course(id: int):
    return await Course_Pydantic.from_queryset_single(Course.get(id=id))

@course_router.put("/api/course/{id}", response_model=Course_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_a_course(id: int, course: CourseIn_Pydantic):
    await Course.filter(id=id).update(**course.dict(exclude_unset=True))
    return await Course_Pydantic.from_queryset_single(Course.get(id=id))


@course_router.delete("/api/course/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete_a_course(id: int):
    delete_obj = await Course.filter(id=id).delete()

    if not delete_obj:
        raise HTTPException(status_code=404, detail="This Course is not found.")
    return Message(message="Successfully Deleted")





