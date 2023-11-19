from pydantic import BaseModel
from datetime import datetime


class OperationCreate(BaseModel):
    id: int
    datetime: datetime
    title: str
    x_avg_count_in_line: float
