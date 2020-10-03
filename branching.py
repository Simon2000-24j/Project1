cities = ['Москва', 'Париж', 'Лондон']

new_city = 'Нью-Йорк'

if new_city not in cities:
    cities.append(new_city)
    print('Город добавлен в список')
else:
    print('Город не добавлен в список')

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Софья', 'age': 20}]

new_user = {'name': 'Пётр', 'age': 25}

if new_user not in users:
    users.append(new_user)
    print('Пользователь добавлен в список')
else:
    print('Пользователь не добавлен в список')

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]

new_tourist = {'user': users[3], 'city': cities[3]}

if new_tourist not in tourists:
    tourists.append(new_tourist)
    print('Турист добавлен в список')
else:
    print('Турист не добавлен в список')

city = input('Введите город: ')
tourist = input('Введите имя туриста: ')
age = input('Введите возраст: ')


print('Турист ', tourist, 'возраст', age, '. ', 'Посетил город', city)
