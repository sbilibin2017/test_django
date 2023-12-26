import os

from pydantic import BaseModel, Field

PREFIX = "POSTGRES"


class DBSettings(BaseModel):
    db: str = Field(default=os.environ.get(f"{PREFIX}_DB"))
    user: str = Field(default=os.environ.get(f"{PREFIX}_USER"))
    password: str = Field(default=os.environ.get(f"{PREFIX}_PASSWORD"))
    host: str = Field(default=os.environ.get(f"{PREFIX}_HOST"))
    port: str = Field(default=os.environ.get(f"{PREFIX}_PORT"))
    schema_name: str = Field(default=os.environ.get(f"{PREFIX}_SCHEMA"))

    class Config:
        frozen = True
