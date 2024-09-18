from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.models import Course, Course_Pydantic


page_router = APIRouter()

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@page_router.get("/", response_class=HTMLResponse, name="home")
async def home_page(request:Request):
    course_list = await Course_Pydantic.from_queryset(Course.all())

    return templates.TemplateResponse(name ="home.html", request = request, context={"course_list": course_list})


@page_router.get("/about", response_class=HTMLResponse, name="about")
async def about_page(request:Request):
    return templates.TemplateResponse(name = "about.html", request = request)



@page_router.get("/courses", response_class=HTMLResponse, name="courses")
async def course_page(request:Request):
    course_list =  await Course_Pydantic.from_queryset(Course.all())
    return templates.TemplateResponse(name = "course.html", request = request, context= {"course_list":course_list})


@page_router.get("/courses/{course_id}", response_class=HTMLResponse, name = "course_detail")
async def course_detail_page(request: Request, course_id: int):
    # Query a single course by its ID
    course = await Course_Pydantic.from_queryset_single(Course.get(id=course_id))

    # Pass the course to the detail template
    return templates.TemplateResponse("course_detail.html", context={"course": course, "request": request})



@page_router.get("/contact", response_class=HTMLResponse, name="contact")
async def contact_page(request:Request):
    return templates.TemplateResponse(name = "contact.html", request = request)
