import requests

class Human:
    pass

def my_func():
    pass


rq = requests

jack = Human

print(requests.__name__)
print(rq.__name__)
print(jack.__name__)
print(Human.__name__)
print(__name__)

print(type(rq))
print(type(Human))
#dir()
list_cars = ["tesla", "toyota", "bmw"]

for method in dir(list_cars):
    #print(method, getattr(list_cars, method))
    print(method)

print("==========================")

for method in dir():
    print(method)

data = "string"


print("========================")
print(hasattr(data, "reverse"))
print(hasattr(data, "replace"))

print("==============")
print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))

print("=========================")

print(callable(data))
print(callable(my_func))
print(callable(list_cars))

print("===================")

class First:
    pass

class Second(First):
    pass

print(issubclass(First, Second))
print(issubclass(Second, First))
print("=====================")
first = First()
second = Second()


print(isinstance(first, Second))
print(isinstance(second, First))
print("===============================")

print("===INSPECT===")
import inspect
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

print("=====================")
class Human:
    def __init__(self, age, name="Jack"):
        self.name = name
        self.age = age

s_human = inspect.signature(Human)
for param in s_human.parameters.values():
    print(param.name, "=", param.default)
    print("--------------")

print("====sys=====")

import sys

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

print("================================")
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)












