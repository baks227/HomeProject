from sqlalchemy import create_engine
from models import Base
import Conf

# Замените на свои данные подключения
DATABASE_URL=Conf.connect()

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("База данных успешно создана!")
