from sqlalchemy import create_engine, insert, delete, update, select
from workers import read_csv, serializer
from models import Base, Car, Toy

engine = create_engine("sqlite:///./db.sqlite3", echo = True)
Base.metadata.create_all(engine)

# Create
def create(table, new_car: dict) -> dict:
    with engine.connect() as conn:
        stmt = insert(table).values(new_car)
        conn.execute(stmt)
        conn.commit()
    return new_car

# Read
def read(table) -> list:
    rows: list = []
    data: list = []
    with engine.connect() as conn:
        stmt = select(table)
        rows = conn.execute(stmt)
    for row in rows:
        data.append(row)
    return data

def read(table, name: str) -> list:
    rows: list = []
    data: list = []
    with engine.connect() as conn:
        stmt = select(table).where(table.name == name)
        rows = conn.execute(stmt)
    for row in rows:
        data.append(row)
    return data

# Update
def update(table, name: str, new_car: dict = {}) -> dict:
    with engine.connect() as conn:
        stmt = update(table).where(table.name == name).values(new_car)
        conn.execute(stmt)
        conn.commit()
    return name

# Delete
def delete(table, name: str) -> dict:
    with engine.connect() as conn:
        stmt = delete(table).where(table.name == name)
        conn.execute(stmt)
        conn.commit()
    return name

data = read_csv("data.csv")
records = serializer(data, ["name", "mark", "price", "speed"])
for record in records:
    create(Car, record)