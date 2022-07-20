from pydantic import BaseModel, Field

from config import model_settings


class CodeRequest(BaseModel):
    code: str = Field(
        default="print(",
        description="first words for code to generate",
    )
    max_length: int = Field(
        default=model_settings.model_min_length,
        description="length of generating code",
    )
