#!/usr/bin/python3
from models.place import Place

print(type(Place.city_id) is str)
print(Place.city_id == "")

print(type(Place.user_id) is str)
print(Place.user_id == "")

print(type(Place.name) is str)
print(Place.name == "")

print(type(Place.description) is str)
print(Place.description == "")

print(type(Place.number_rooms) is int)
print(Place.number_rooms == 0)

print(type(Place.number_bathrooms) is int)
print(Place.number_bathrooms == 0)

print(type(Place.max_guest) is int)
print(Place.max_guest == 0)

print(type(Place.price_by_night) is int)
print(Place.price_by_night == 0)

print(type(Place.latitude) is float)
print(Place.latitude == 0)

print(type(Place.longitude) is float)
print(Place.longitude == 0)
