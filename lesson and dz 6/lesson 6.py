# res = 5/0
# print("Hello World")
# print(res)
# print("End code")
# ctrl+/

print("==========Base Exception==============")

print(f"nameError = {type(NameError)} - {issubclass(NameError, BaseException)}")

try:
    print(hello)
except NameError:
    print("NameError")


try:
    print(int(input("enter first num - "))/int(input("enter second num - ")))
except ZeroDivisionError:
    print("ZeroDivisionError - what are you doing?")
except ValueError as e:
    print("ValueError - enter only numbers!", end = "")
    print(e)



try:
    list_color = ["red", "green", "blue"]
    print(list_color[10])
except (IndexError, NameError) as error:
    print("IndexError - something went wrong", end = "")
    print(error)

print("=========================================")

try:
    print(hello)
    print("Hello World")
except NameError as error:
    print("Something went wrong")
else:
    print("no problem")
finally:
    print("Finally code")

print("=========================================")

print("End code")
