#3.1,3.2
# names = ['andrey','Anton','Yasha','sasha']
#
# for name in names:
#     print(f'Hi,my dear friend, {name.title()}')
#
#3.3
# cars = ['toyota','bmv','tesla','porshe']
#
# for car in cars:
#     print(f'Я хочу себе машину {car.title()}')
#

#3.4-3.7
guests=['stalin','beria','trotskii','lenin']
#
# def gosti(a):
#     for guest in a:
#         print(f'Hi,dear guest {guest.title()}')
# #gosti(guests)
# print(f'\nочень жаль что не придешь {guests.pop(-1).title()}\n')
# guests.append('iagoda')
# #gosti(guests)
# #print('\nя купил новый стол\n')
# guests.insert(0,'marks')
# guests.insert(2,'brejnev')
# guests.append('engels')
# #gosti(guests)
#
# print('sorry')
#
# while len(guests) > 2:
#     remove_goust=guests.pop()
#     print(f'Ssory, no you {remove_goust.title()}')
# print(guests)
# for guest in guests:
#     print(f'Hi,dear guest {guest.title()}')
#
# del guests[0]
# del guests[0]
# print(guests)

#3.8-3.10
countries = ['tailand', 'germany', 'usa',  'canada', 'china']

# print(sorted(countries))
# print(countries)
# print(sorted(countries, reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)
#
# print(f'На ужин приглашено {len(guests)} гостей')

# print(sorted(countries))
# print(countries)
# print(sorted(countries, reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)
# print(countries.pop())
# countries.append('india')
# print(countries)
# countries.insert(-1,'japan')
# print(countries)
# del countries[-1]
# print(countries)
# countries.remove('usa')
# print(countries)
# print(len(countries))
# print(countries)
#8
#4.1-4.2
pizzas=['piperoni', 'margarita', 'bianca']
# for pizza in pizzas:
#     print(f'this my like type pizza {pizza.title()}\n')
# print('I like pizza')

#4.3-4.9
# for item in range(1,21):
# #     print(item)
#
# mil = list(range(1,1000001))
# # for item in mil:
# #     print(item)
# print(max(mil), min(mil), sum(mil))
# # for item in range(1,21,2):
# #     print(item)
# three = list(range(3,31,3))
# print(three)
# for item in three:
#     print(item)
# for item in range(1,11):
#     print(item**3)
# squares = [item ** 3 for item in range(1,11)]
# print(squares)

#4.10-4.12
# elements = [item for item in range(10)]
# print(elements)
# print(f'Первые три пункта в списке - {elements[:3]}')
# print(f'Три пункта в середине списка - {elements[3:6]}')
# print(f'Последние три пункта в списке - {elements[-3:]}')
#
# friend_pizzas = pizzas[:]
# pizzas.append('sea')
# friend_pizzas.append('burger')
#
# for pizza in pizzas:
#     print(pizza)
#
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)
#
# if pizzas == friend_pizzas:
#     print('ok')
# else:
#     print('not ok')