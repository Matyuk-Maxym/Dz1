
class JackNameError(Exception):
    def __init__(self, name):
        self.name = name
        print(name)

    def __str__(self):
        return f"{self.name} is an invalid name"

    def __str__(self):
        return  "JackNameError"





def check_name():
    name = input("Enter your name: - ")
    if name.lower() == "jack":
        raise JackNameError("Jack isn`t good!!!")
    else:
        print(name, "is good name")
check_name()
