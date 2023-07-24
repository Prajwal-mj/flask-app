# object oriented programming 
# data structures & algorithms 

# built-in data structures
# arrays, lists, dictionaries

# user defined data structures 
'''
1. Linked List 
2. Queue
3. Stack
4. Binary Tree, Tree
5. Heap
'''
'''
class <class-name>:

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def fun_1(self):
        return
    def fun_2(self, var1):
        ...
        return

'''

class Car:

    def __init__(self, name, color):
        self.speed = 0
        self.name = name
        self.color = color

    def SetSpeed(self, speed):
        self.speed = speed
        

car_1 = Car('scorpio', 'black')
car_2 = Car('Alto', 'white')

print(car_1.speed)

car_1.speed = 10

print(car_1.speed)

car_1.SetSpeed(20)

print(car_1.speed)

