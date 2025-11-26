from pydantic import BaseModel
from datetime import datetime

class NoticeBase(BaseModel):
    title: str
    content: str | None = None

class NoticeCreate(NoticeBase):
    pass

class Notice(NoticeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True