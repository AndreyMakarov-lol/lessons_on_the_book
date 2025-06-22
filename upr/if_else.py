# #5.1-5.2
# car = 'subaru'
# if car == 'subaru':
#     print('car==subaru')
#     print(car == 'subaru')
# if car != 'audi':
#     print('it not subaru')
#     print(car == 'audi')
#
# string1 = 'govno gopa'
# string2 = 'gavno gopa'
# string3 = 'Govno gopA'
#
# if string1 != string2:
#     print(string1 == string2)
#
# if string1 == string1:
#     print(string1 == string1)
#
# if string3.lower() == string1:
#     print(string3.lower() == string1)
# if string3 != string1:
#     print(string3 == string1)
# if 1 < 2:
#     print('1 < 2')
# if 1 > 2:
#     pass
# else:
#     print('1 > 2')
# if 2 <= 2:
#     print('2 <= 2')
# if 2 >= 2:
#     print('2 >= 2')
#
# if 1==1 and 2==2:
#     print('1==1 and 2==2')
#
# if 1==1 or 2==3:
#     print('1==1 or 2==3')
#
# names = ['Andrew', 'Sam', 'Igor']
# user1 = 'Sam'
# user2 = 'John'
#
# if user1 in names:
#     print(f'{user1} in names')
# if user2 not in names:
#     print(f'{user2} not in names')

# 5.3-5.9
# alien_color = 'red'
# if alien_color == 'green':
#     print('you have 5 points')
# else:
#     print('you have 10 points')
#
# if alien_color == 'govno':
#     pass
#
# if alien_color == 'green':
#     print('you have 5 points')
# elif alien_color == 'yellow':
#     print('you have 10 points')
# elif alien_color == 'red':
#     print('you have 15 points')

# age = int(input('Введи возраст '))
# if age < 2:
#     print('младенец')
# elif 2 <= age < 4:
#     print('малыш')
# elif 4 <= age < 13:
#     print("ребенок")
# elif 13 <= age < 20:
#     print("подросток")
# elif 20 <= age < 65:
#     print("ребенок")
# else:
#     print('Пожилой человек')
#
#
# frut = ['banana', 'apple','lime']
#
# if 'gay' in frut:
#     print("gay")
# elif 'banana' in frut:
#     print("you like banana")

# users = []
#
#
# if users:
#     user = str(input('Введите имя '))
#     if user == 'admin':
#         print('Привет админ')
#     else:
#         print(f'привет {user}')
# else:
#     print('нужны юзеры')



#https://youtube.com/shorts/GyfEwpIL4Ys?si=wj5R4ieX950ydeTK

#5.10-5.11
# current_users = ['Kolya', 'lena', 'olya', 'egor', 'John']
# new_users = ['ira', 'john', 'yana', 'adolf']
#
# for new_user in new_users:
#     current_users_lower = [name.lower() for name in current_users]
#     if new_user.lower() in current_users_lower:
#         print('такой юзер уже есть')
#     else:
#         print(f'привет {new_user}')
#

# nums = [num for num in range(1,10)]
#
# for num in nums:
#     if num == 1:
#         print(f'{num}st')
#     elif num == 2:
#         print(f'{num}nd')
#     elif num == 3:
#         print(f'{num}sd')
#     else:
#         print(f'{num}th')

#6.1-6.8
# person = {
#     'first_name' : 'jenia',
#     'last_name' : 'makarova',
#     'city' : 'kyrchatov',
# }

# for key , value in person.items():
#     print(f'it s key {key}, it value {value}\n')


# nums = {
#     'jenia' : 1,
#     'anton' : 3,
#     'andrey' : 56,
#     'yasha' : 1488,
#     'hz' : 0

# }
# for key , value in nums.items():
#     print(f'it s key {key}, it value {value}\n')

# golosariy = { 
#     'python' : 'Язык програмирования, интерпретируемый, с простым синтаксисом',
#     'интерпретатор' : 'программа транслирующая для исполнения компьютером инструкции',
#     'словарь' : 'тип множества, прмнящий для хранения значения  в виде пары ключ-значение',
#     'строка' : 'тип данных в которых хранится информация в виде набора символов',
#     'интеджер' : 'тип данных для хранения простых чиел'
# }

# for termin, value in golosariy.items():
#     print(f'{termin.title()}:')
#     print(f'{value.capitalize()}.\n')

# languages = {
#     'kolya' : 'c',
#     'andrey' : 'python',
#     'jenia' : 'rust'
# }

# persons = ['vania', 'kolya', 'olya', 'andrey', 'lena', 'jenia']

# for item in persons:
#     if item in languages.keys():
#         print(f'{item.title()} ты уже голосовал(а)\n')
#     else:
#         print(f'{item.title()} проголосуй\n')

# person_1 = {
#     'first_name' : 'jenia',
#     'last_name' : 'makarova',
#     'city' : 'kyrchatov',
# }

# person_2 = {
#     'first_name' : 'andrey',
#     'last_name' : 'makarov',
#     'city' : 'kyrchatov',
# }

# person_3 = {
#     'first_name' : 'saha',
#     'last_name' : 'mmerkulov',
#     'city' : 'kyrsk',
# }

# persons = [person_1, person_2, person_3]

# for person in persons:
#     full_name = f'Full name {person['first_name'].title()} {person['last_name'].title()}'
#     city = f'City: {person['city'].title()}'
#     print(full_name, city)
#6.8-6.12
# dog = {
#     'name' : 'rex',
#     'type' : 'dog',
#     'boss' : 'andrey'
# }
# gosha = {
#     'name' : 'gosha',
#     'type' : 'parrot',
#     'boss' : 'andrey'
# }
# shiskin = {
#     'name' : 'shiskin',
#     'type' : 'sqerel',
#     'boss' : 'andrey lobodin'
# }
#
# pets = [dog, gosha, shiskin]
#
# for pet in pets:
#     print(f"""{pet['name'].title()}
# {pet['type'].title()}
# {pet['boss'].title()}\n""")


# favorite_places = {
#     'ivan' : ['kursk', 'lgov', 'piter'],
#     'lexa' : ['kursk', 'piter'],
#     'kolya' : ['lgov', 'piter'],
# }
#
#
# for name, places in favorite_places.items():
#     print(f"""{name.title()} like to : {', '.join(places)}
#             """)
#
# nums = {
#     'jenia' : [1,4,5],
#     'anton' : [3, 9, 0],
#     'andrey' : [56, 57,87],
#     'yasha' : [1488, 228],
#     'hz' : [0, 1]
#
# }
# for key , value in nums.items():
#     print(f'it s key {key}, it value {value}\n')
#
#
# cities ={
#     'kursk' : {
#         'country' : "Russia",
#         'population' : 1488,
#         'fact' : 'ia ne ottuda',
#     },
#     'kurchatov': {
#         'country': "Russia",
#         'population': 228,
#         'fact': 'ia ottuda',
#     },
#     'belgorod' : {
#         'country': "Russia",
#         'population': 1000,
#         'fact': 'ia tam ucilsia',
#     }
# }
#
#
# for city, info in cities.items():
#     print(f"""It is {city.title()}, and facts
# in country - {info['country'].title()},
# it population - {info['population']},
# it fact - {info['fact'].capitalize()}\n""")

#7.1-7.2
# car=input('Какую тачку хочешь?\n')

# print(f'Щас гляну есть ли {car.capitalize()}')

table = int(input('На сколько мест сол?\n'))

if table < 8:
    print('Стол готов')
else:
    print('Подождать')




























