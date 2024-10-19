#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will trigger the setter for validation
        self.condition = 'New'  # Set the initial condition to 'New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")  # Adjusted output
        self.condition = 'New'  # Reset condition to 'New' after cobbling
