from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "집에가고싶다",
                "image": "path/to",
                "description": "집에빨리가고싶다",
                "tags": ["일본", "가고싶다"],
                "location": "제1실습관 207",
            }
        }
    )