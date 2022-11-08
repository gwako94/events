from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from .database import ref
from .helpers import generate_id


class User(BaseModel):
    """ Todo schema """
    user_id: str = ""
    name: str = ""
    email: str = ""
    gender: str = ""
    region: str = ""
    constituency: str = ""
    person_with_disability: str = ""
    describe_disability: str = ""
    innovation_name: str = ""
    category: str = ""
    entry_type: str = ""
    innovation_period: str = ""
    team_members: list = []
    founder_age: str = ""
    project_description: str = ""
    problem_targeted: str = ""
    current_solution: str = ""
    target_market: str = ""
    twitter: str = ""
    facebook: str = ""
    linkedin: str = ""
    github_profile: str = ""


route = FastAPI()

origins = [
    "https://neinnovationweek.co.ke/",
    "http://localhost",
    "http://localhost:3000",
]

route.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@route.post("/register")
async def register(user: User):
    user_dict = user.dict()
    if user:
        user_id = generate_id()
        user_dict.update({"user_id": user_id})
        ref.child(user_id).set(user_dict)
        return {"message": "user registered!"}


@route.get("/users")
async def get_users():
    try:
        users = [value for value in ref.get().values()]
        return {"users": users}
    except Exception as e:
        return {"users": []}
