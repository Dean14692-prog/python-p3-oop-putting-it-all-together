#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        
       
        

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        
        if not isinstance(value, int):
            print("size must be an integer")

        else:
            self._size = value
    
    def cobble(self):
        # return 'the shore has been repaired'
        print("Your shoe is as good as new!")
        self.condition = "New"

    

stan_smith = Shoe('Adidas', 9)