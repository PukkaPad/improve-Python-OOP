# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Vehicle (object):

    """A vehicle for sale at a dealership.

    Attributes:
    wheels: integer that represents the number of wheels
    miles: number of miles driven on the vehicle
    make: string of the make of the vehicle
    model: model of the vehicle as a string
    year: year the vehicle was built
    sold_on: the date the vehicle was sold
    """

    __metaclass__ = ABCMeta
    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Vehicle object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this Vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the Vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 8000 - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass

    #@staticmethod
    #def make_car_sound():
    #    print("Vroommm! Bibi..Fonfon!!!")

    #@classmethod
    #def is_motorcycle(cls):
    #    return cls.wheels == 2

class Car(Vehicle):
    """A car for sale by the dealer."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by the dealer."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'

class Motorcycle(Vehicle):
    """A motorcycle for sale by the dealer."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'

#wheels, miles, make, model, year, sold_on
mustang = Car(4, 190000, 'Ford', 'Mustang', 2010, 2015)
print (mustang.wheels)
print (Car.wheels)