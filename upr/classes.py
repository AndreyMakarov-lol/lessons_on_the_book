class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print(f'Today {self.restaurant_name} it s open')

restaurant = Restaurant('Jopa', 'japan')

restaurant.describe_restaurant()
restaurant.open_restaurant()