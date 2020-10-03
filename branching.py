city = input('Введите город: ')
cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]



if city == 'ПаРиж':
     print (f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город {cities[1]}") 
if city == 'париЖ':
     print (f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город {cities[1]}")      
if cities[0]== city :
     print(f"Турист {users[0]['name']} возраст {users[0]['age']}. Посетил город {cities[0]}")
if cities[1] == city : 
     print (f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город {cities[1]}")  
if cities[2] == city :  
     print (f"Турист {users[2]['name']} возраст {users[2]['age']}. Посетил город {cities[2]}")
