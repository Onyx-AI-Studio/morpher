from typing import Any

from pydantic import BaseModel


class Tool(BaseModel):
    name: str
    description: str

    # def __init__(self, name: str, description: str, **data: Any):
    #     super().__init__(**data)
    #     self.name = name
    #     self.description = description
