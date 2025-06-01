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

print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print(countries.pop())
countries.append('india')
print(countries)
countries.insert(-1,'japan')
print(countries)
del countries[-1]
print(countries)
countries.remove('usa')
print(countries)
print(len(countries))
print(countries)