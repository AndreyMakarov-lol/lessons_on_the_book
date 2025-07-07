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