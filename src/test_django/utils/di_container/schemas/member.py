from pydantic import BaseModel


class MemberDTO(BaseModel):
    name: str
    signature: str
