#9.1-9.2
# class Restaurant:
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name}, {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f'Today {self.restaurant_name} it s open')
#
# restaurant = Restaurant('Jopa', 'japan')
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

#9.3
# class User:
#     def __init__(self, first_name, last_name, age, country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.country = country
#
#     def describe_user(self):
#         print(f'Name: {self.first_name.title()} {self.last_name.title()}\n'
#               f'Age: {self.age}\nCountry: {self.country.title()}')
#
#     def greet_user(self):
#         print(f'\nWelcome dear {self.first_name.title()} {self.last_name.title()}')
#
# user_1=User('Andrey', 'Makarov', 29, 'russia')
# user_2 = User('jenia', 'sukanova', 16, "russia")
#
# user_1.describe_user()
# user_1.greet_user()
#
# user_2.describe_user()
# user_2.greet_user()

#9.4

# class Restaurant:
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()}, {self.cuisine_type}, served {self.number_served}")
#
#     def open_restaurant(self):
#         print(f'Today {self.restaurant_name} it s open')
#
#     def set_number_served(self, served_new):
#         self.number_served = served_new
#
#     def increment_number_served(self, add_served):
#         if add_served > 0:
#             self.number_served += add_served
#         else:
#             print("ТЫ ЧЕ ДЕЛАЕШЬ, ЧЕРТ ЕБАНЫЙ")
#


# restaurant = Restaurant('burger king', 'fast food')
#
# restaurant.describe_restaurant()
# restaurant.set_number_served(10)
# print(restaurant.number_served)
# restaurant.increment_number_served(10)
# print(restaurant.number_served)
# restaurant.increment_number_served(-10)
# print(restaurant.number_served)


#9.5
#
# class User:
#     def __init__(self, first_name, last_name, age, country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.country = country
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f'Name: {self.first_name.title()} {self.last_name.title()}\n'
#               f'Age: {self.age}\nCountry: {self.country.title()}')
#
#     def greet_user(self):
#         print(f'\nWelcome dear {self.first_name.title()} {self.last_name.title()}')
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# new_user = User('Jopa', 'Popa', 1488, 'iran')
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.reset_login_attempts()
# print(new_user.login_attempts)


# #9.6
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# #!!!Работает только при разблокированном классе упражнение 9.4!!!
#
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors
#
#     def flavors_ice_cream(self):
#         print(f' flavor: {self.flavors}')
#
#
# restaurant_ice = IceCreamStand('burger king', 'fast food',['chocolate','milk'])
#
# restaurant_ice.describe_restaurant()
# restaurant_ice.flavors_ice_cream()