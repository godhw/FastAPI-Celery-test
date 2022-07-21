from pydantic import BaseModel


class CodeResponse(BaseModel):
    text: str
