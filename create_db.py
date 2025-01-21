from sqlalchemy import create_engine
from models import Base

# Замените на свои данные подключения
DATABASE_URL = "postgresql://postgres:Qq-123456@127.0.0.1:5432"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("База данных успешно создана!")
