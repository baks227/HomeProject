import seed_data

# создание пользователя
username = str(input('Введите ваше иня: '))
email = str(input('Введите вашу электронную почту: '))
password = str(input('Введите ваш пароль: '))

n = 9
while n != 0:
    print('Выберите действие:\n1-Создание уникальной учетной записи '
          '\n2-Составление заказа'
          '\n3-Просмотр заказа пользователя'
          '\n0- завершение работы')
    n=int(input())
    k=[]
    if n == 1:
        gen_user = seed_data.add_user(username, email, password)
        print('Пользователь успешно создан!!!')
    #elif n == 2:
        #qap=int(input('Введите количество товаров, которое планируете купить: '))
        #prod = []
        #while qap!=0:
            #print('Выберите товар:\n1 - PC мощный для работы и игр'
            #     '\n2- Laptop мощный для работы и игр'
            #      '\n3- Server Самый Мощный самый лучший'
            #      '\n4- Portale Современный портативный компьютер'
            #      '\n5- Assembly Сборка компьютера/n')
            #buy_item = int(input())
            #if buy_item == 1:
              #  prod.append(seed_data.PC)
            #elif buy_item == 2:
             #   prod.append(seed_data.Laptop)
            #elif buy_item ==3:
            #    prod.append(seed_data.Server)
           # elif buy_item ==4:
           #     prod.append(seed_data.Portable)
           # elif buy_item ==5:
            #    prod.append(seed_data.Assembly)
           # qap-=1
          #  qai = int(input('Введите количество единиц, которое планируете купить: '))
         #   k.append(qai)
        #gen_order = seed_data.add_order(prod,k)
       # print('Заказ успешно создан.')
    #elif n==3:
     #   print('Финальная цена к оплате\n')
      #  gen_Total_price = seed_data.total_price(username)


