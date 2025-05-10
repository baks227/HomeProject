
def connect():
    login = input('Введите логин для подключения: ')
    passw = input('Введите пароль для подключения: ')
    adress = input('Введите адрес соединения:порт: ')
    DATABASE_URL = f"postgresql://{login}:{passw}@{adress}"
    return DATABASE_URL

#"postgresql://postgres:Qq-123456@127.0.0.1:5432"