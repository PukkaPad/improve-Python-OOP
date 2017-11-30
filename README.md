# Revising Python OOP

Revising and improving OOP with Python.

## Class:

Logical grouping of data and functions. Blueprint for creating objects.

`Class Customer(object):` does not create a new customer. It defines the customer. It's the blueprint to create a Customer object.

A customer would be created as follows:

` john = Customer('Jhoon Smith', 1025.0)`

So as I have showed, to create the new customer the `__init__` method is called (without `self`). john is an **object**, known as *instance*.

`self` is the *instance*. Which means that calling `jhon.withdraw(100.0)` puts the instructions on the *john* instance. `Customer.withdraw(jhon, 100.0)` is the same as `jhon.withdraw(100.0)`.

After `__init__` has finished, the object *jhon* is ready to be used. Then `deposit` and `withdraw`call can be made.

* static methods hold for all instances. They are not introduced by the `__init__` method. The `@staticmethod` decorator is used.

* instance methods: `class Vehicle (object): ` has the attribute `wheels` that can be accessed using `self.wheels`.

* class methods: methods not bound to an object, but to a class.

### Inheritance

Great for code re-usability and extensibility. Class can inherit access to data fields and methods, and I can write my own methods and fields without needing to rewrite everything.

If class X extends to class Y, Y = super class and X = sub class.

Class X derives the data and behavior of the class Y.
wheels, miles, make, model, year, sold_on
The parent class should be an Abstract Base Class (ABC). ABC classes are only meant to be inherit from, instances cannot be created.