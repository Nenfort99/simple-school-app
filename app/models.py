from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from datetime import datetime

class Course(Model):
    id = fields.IntField(pk=True)  # Primary key
    title = fields.CharField(max_length=255)  # Post title
    description = fields.TextField()  # Post content
    author = fields.CharField(max_length=100)  # Author name
    price = fields.FloatField(null=True )
    created_at = fields.DatetimeField(auto_now_add=True)  # Automatically set to current time on creation
    updated_at = fields.DatetimeField(auto_now=True)  # Automatically updates when the record is modified
    is_published = fields.BooleanField(default=True)  # Optional field to mark post as published or not



    def __str__(self):
        return self.title

    class PydanticMeta:
        table = "courses"  # Set the table name in the database





Course_Pydantic = pydantic_model_creator(Course, name="Course")
CourseIn_Pydantic = pydantic_model_creator(Course, name="CourseIn", exclude_readonly=True)




TORTOISE_ORM = {
    "connections": {
        # "default": "asyncpg://jamezslim90:zmgHh7aNwQk9@ep-cold-leaf-25567838.us-west-2.aws.neon.tech/fastapi-school-app"
        "default": "asyncpg://nenforthdb_owner:ze2sC5OkQZcS@ep-twilight-moon-a29n3ju9.eu-central-1.aws.neon.tech/nenforthdb"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # Include Aerich models
            "default_connection": "default",
        },
    },
}
