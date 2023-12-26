import os

from pydantic import BaseModel, Field

PREFIX = "REDIS"


class CacheSettings(BaseModel):
    password: str = Field(default=os.environ.get(f"{PREFIX}_PASSWORD"))
    db: str = Field(default=os.environ.get(f"{PREFIX}_DB"))
    host: str = Field(default=os.environ.get(f"{PREFIX}_HOST"))
    port: str = Field(default=os.environ.get(f"{PREFIX}_PORT"))

    class Config:
        frozen = True
