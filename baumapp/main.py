from enum import Enum
from typing import List, Optional
from fastapi import FastAPI, Request, status
from datetime import datetime
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError

from pydantic import BaseModel, Field, ValidationError

from baumapp.auth.auth import auth_backend
from baumapp.auth.schemas import UserRead, UserCreate
from baumapp.auth.manager import get_user_manager
from fastapi_users import FastAPIUsers
from baumapp.database import User
from baumapp.router import router as router_baumapp

dt1 = datetime.now()
dt2 = datetime.now()
dt3 = datetime.now()

app = FastAPI(
    title='baum-app'
)


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail': exc.errors()})
    )


# fake_books = [
#     {'id': 1, 'datetime': dt1, 'title': 'Very fun book', 'avg_x': 0.12, 'genre': 'novel'},
#     {'id': 2, 'datetime': dt2, 'title': 'Sad book', 'avg_x': 0.01, 'genre': 'poem'},
#     {'id': 3, 'datetime': dt3, 'title': 'Simple funny book', 'avg_x': 0.005},
# ]

# class GenreChoice(Enum):
#     novel = 'novel'
#     poem = 'poem'


# class Book(BaseModel):
#     id: int
#     datetime: datetime
#     title: str = Field(max_length=100)
#     avg_x: float = Field(ge=0)
#     genre: Optional[GenreChoice] = None



# @app.get('/books/{book_id}', response_model=List[Book])
# def get_book(book_id: int):
#     return [book for book in fake_books if book['id'] == int(book_id)]

# @app.get('/books/')
# def get_books_list(limit: int = 1, offset: int = 1):
#     return fake_books[offset:][:limit]

# @app.post('/books/{book_id}')
# def change_book_title(book_id: int, new_title: str):
#     current_book = list(filter(lambda book: book.get('id') == book_id, fake_books))[0]
#     current_book['title'] = new_title
#     return {'status': 200, 'data': current_book}

# @app.post('/books/')
# def add_book(books: List[Book]):
#     fake_books.extend(books)
#     return {'status': 200, 'data': fake_books}

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),

)

app.include_router(router_baumapp)


current_user = fastapi_users.current_user()

@app.get('/protected-route')
def protected_route(user: User = Depends(current_user)):
    return f'Hello, {user.username}'

@app.get('/unprotected-route')
def protected_route():
    return f'Hello, anonym'
