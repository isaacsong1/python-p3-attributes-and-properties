#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Random", breed="Mastiff"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) is str) and (1 < len(name)) and (len(name) < 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    # name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)


# import ipdb; ipdb.set_trace()
