from pydantic import BaseModel


class RegistrationDTO(BaseModel):
    interface: type
    implementation: type
