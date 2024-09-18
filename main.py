from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.pages_routes import  page_router
from app.course_routes import course_router
from fastapi.staticfiles import StaticFiles


# Initialise our fastapi app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Include routers
app.include_router(page_router)
app.include_router(course_router)




# # Register Tortoise ORM
register_tortoise(
    app,
    # db_url="sqlite://db.sqlite3",
    db_url= "asyncpg://nenforthdb_owner:ze2sC5OkQZcS@ep-twilight-moon-a29n3ju9.eu-central-1.aws.neon.tech/nenforthdb",
    modules={"models": ["app.models", "aerich.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)



# Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     # Update with specific origins in production
#     allow_origins=["localhost"],
#     allow_methods=["GET", "POST"],
# )