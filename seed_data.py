from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Product, User, Order, OrderItem
import Conf

DATABASE_URL=Conf.connect()

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Добавление категорий
complite = Category(name="Компьютерная техника", description="Готовые сборки")
castom = Category(name="сборка", description="Для энтузиастов")
session.add_all([complite, castom])
session.commit()

# Добавление продуктов
PC = Product(name="Персональный компьютер", description="Мощный компьютер для работы и игр.", price=999.99, stock=50,
             category=complite)
Laptop = Product(name="Ноутбук", description="Мощный ноутбук для работы и игр", price=999.99, stock=50,
                 category=complite)
Server = Product(name="Сервер", description="Самый Мощный самый лучший", price=1999.99, stock=100,
                 category=complite)
Portable = Product(name="Портативный", description="Современный портативный компьютер", price=599.99, stock=75,
                     category=complite)
Assembly = Product(name="Сборка комьютера", description="Цена за услугу", price=19.99, stock=200, category=castom)
session.add_all([PC,Laptop,Server, Portable, Assembly])
session.commit()


# Добавление пользователя
def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    return user


# Создание заказа
def add_order(product,qantity_item):
    total: float = (sum((product[i]).price*int(qantity_item[i]) for i in range(0, len(product))))
    order = Order(user=User.username, total_price=total)
    session.add(order)
    session.commit()
# Добавление позиций заказа
    order_items=[]
    while len(product) !=0:
        order_items.append(OrderItem(order=order, product=product[0], quantity=qantity_item[0]))
        # += float(product.price)
        qantity_item.pop(0)
        product.pop(0)
    session.add_all(x+',' for x in order_items)
    session.commit()
    return order, order_items

print("Тестовые данные успешно добавлены!")
