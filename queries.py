from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Product, User, Order, OrderItem

DATABASE_URL = "postgresql://postgres:Qq-123456@127.0.0.1:5432"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Пример 1: Получение всех продуктов
products = session.query(Product).all()
for product in products:
    print(f"Товар: {product.name}, Цена: {product.price}")

# Пример 2: Получение продуктов определенной категории
Computers_products = session.query(Product).join(Category).filter(Category.name == "Компьютерная техника").all()
print("\nТовары в категории 'Компьютерная техника':")
for product in Computers_products:
    print(f"- {product.name}")

# Пример 3: Получение заказов пользователя
user = session.query(User).filter_by(username='john_doe').first()
user_orders = session.query(Order).filter_by(user=user).all()
print(f"Заказы пользователя {user.username}:")
for order in user_orders:
    print(f"Заказ №{order.id}, Сумма: {order.total_price}")

# Пример 4: Получение деталей заказа
order = session.query(Order).first()
order_items = session.query(OrderItem).filter_by(order=order).all()
print(f"\nДетали заказа №{order.id}:")
for item in order_items:
    print(f"- {item.product.name}, Количество: {item.quantity}")

session.close()