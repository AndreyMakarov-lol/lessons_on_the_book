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
