'''
M03_Lab.py
Created by Julian Payne
This program defines two classes, one being the parent class Vehicle and the other
being the child class Automobile. The Vehicle class is given the attribute type of car
that is inherited by the Automobile class upon instantiation. The Automobile class
will also prompt the user to enter various input to store values related to the car's 
details. It will then print the string representation of this object to the user.

self.type = string variable that stores the type of vehicle
self.year = string variable that stores the year of the vehicle
self.make = string variable that stores the make of the vehicle
self.model = string variable that stores the model of the vehicle
self.doors = string variable that stores the number of doors on the vehicle
self.roof = string variable that stores the type of roof 
new_car = variable that stores the Automobile object
'''

class Vehicle:

    def __init__(self):
        self.type = "car"



class Automobile(Vehicle):

    def __init__(self):
        super().__init__()
        self.year = input("Enter the year of your vehicle: ")
        self.make = input("Enter the make of your vehicle: ")
        self.model = input("Enter the model of your vehicle: ")
        self.doors = input("Enter the number of doors on your vehicle: ")
        self.roof = input("Does your vehicle have a solid roof or a sun roof?: ")

    def __str__(self):
        return f'Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}'

        


def main():
    new_car = Automobile()
    print(new_car)

if __name__ == '__main__':
    main()