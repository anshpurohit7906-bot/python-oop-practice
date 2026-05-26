import numpy as np

class ArrayMath:

    def __init__(self ,initial_list):
        self.numbers = np.array(initial_list)

    def add_to_all(self , value):
        self.numbers = self.numbers + value

    def multiply(self , factor):
        self.numbers = self.numbers * factor

    
my_box = ArrayMath([1,2,3,4,5])
my_box.multiply(10)
my_box.add_to_all(5)
print(my_box.numbers)