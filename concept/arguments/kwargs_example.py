def calculate(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)  # {'add': 3, 'multiply': 5}
    print(kwargs["add"])
    print(kwargs["multiply"])


calculate(add=3, multiply=5)


def calculate2(n, **kwargs):
    print(kwargs)  # {'add': 5, 'multiply': 6}
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)  # 90


calculate2(10, add=5, multiply=6)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan" ,model="GT-R")

print(my_car.model)