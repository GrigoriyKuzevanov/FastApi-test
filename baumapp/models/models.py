from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Float, TIMESTAMP, ForeignKey, Boolean

metadata = MetaData()

book = Table(
    'book',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('datetime', TIMESTAMP, default=datetime.utcnow),
    Column('title', String, nullable=False),
    Column('x_avg_count_in_line', Float, nullable=False),
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)
