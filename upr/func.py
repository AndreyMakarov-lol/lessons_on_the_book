#8.1
# def display_message():
#     print('Это глава про функции')
# display_message()

# # #8.2
# def favorite_book(title):
#     print(f'Моя любимая книга- {title.capitalize()}')
# title_book=input('Введи название книги: ')
# favorite_book(title_book)


#8.3-8.4
# def make_shirt(size ='L', text = 'I love Hyi'):
#     shirt = f"It`s shirt {size}, and have next text: '{text}'"
#     return shirt
# new_shirt = make_shirt(25, 'Ты хуй')
# print(new_shirt)
# last_shirt = make_shirt()
# print(last_shirt)

#8.5

# def discribe_city(city , country = 'russia'):
#     discribe = f'{city.title()} находится в {country.title()}'
#     print(discribe)
#
# discribe_city('Питер')
# discribe_city('Барселона', 'Испания')
# discribe_city('Париж', 'Франция')

#8.6
# def city_country(city, country):
#     otvet = f'{city.title()}, {country.title()}'
#     return otvet
# def_otvet = city_country('москва','россия')
# print(def_otvet)

# #8.7-8.8
#
# def make_album(name, info, lines='' ):
#     album = {
#         'name': name,
#         'album': info,
#         **({'lines': lines} if lines else {})
#     }
#     return album
#
#
# while True:
#     artist_name = input('Pleas write artist name: ')
#     album_name = input('Pleas write album name: ')
#     lines = input('Pleas write lines nums or no: ')
#     if lines == 'no':
#         new_album = make_album(artist_name, album_name)
#         print(new_album)
#         break
#     else:
#         new_album = make_album(artist_name, album_name, lines)
#         print(new_album)
#         break

#8.9
# messages_text = ['Hui na', 'zyi dva', 'coci tri']
# def show_messages(messages):
#     for message in messages:
#         print(f'{message}')
#
# show_messages(messages_text)
# show_messages(messages_text)
#8.10
# messages_text = ['Hui na', 'zyi dva', 'coci tri']
# send_messages = []
# def show_messages(messages):
#     while messages:
#         message = messages.pop()
#         print(f'Send {message}')
#         send_messages.append(message)
#
# show_messages(messages_text)
# show_messages(messages_text)
# print(send_messages)

#8.11
#
# messages_text = ['Hui na', 'zyi dva', 'coci tri']
# send_messages = []
# def show_messages(messages):
#     while messages:
#         message = messages.pop()
#         print(f'Send {message}')
#         send_messages.append(message)
# show_messages(messages_text[:])
# print(send_messages)
# print(messages_text)


#8.12
# all_toppings = []
# def sendwic(*toppings):
#     print('in sendwich:')
#     for topping in toppings:
#         print(f'- {topping}')
#
# while True:
#     topping_add = input('Write toppings or not: \n')
#     if topping_add != 'not':
#        all_toppings.append(topping_add)
#     else:
#         break
#
# print(all_toppings)
# sendwic(*all_toppings)

#8.13
# def build_profile(first, last, **user_info):
#     user_info['first'] = first
#     user_info['last'] = last
#     return user_info
#
# user_profile = build_profile('Andrey', 'Makarov',
#                              car = 'reno', like = 'beer', wife = 'Jania')
# print(user_profile)
#8.14
# def build_car(creator ,model, **car_info):
#     return {'creator': creator, 'model': model, **car_info}
#
# car = build_car('reno','sandero', color = 'white', type = 'hatchback')
#
# print(f'This {car['creator'].title()}\n'
#       f'Model: {car['model'].title()}')
# for key, value in car.items():
#     if key not in {'creator', 'model'}:
#         print(f'{key.title()}: {value.title()}')

#8.15-16

#import print_models
#from print_models import print_models
#from print_models import print_models as mod
#import print_models as mod
# from print_models import *
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

