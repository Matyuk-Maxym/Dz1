def checker(function):

    def checker(*args, **kwargs):
        try:
            res = function(*args, **kwargs)
        except Exception as e:
            print(e)
        else:
            print(f"No problems. Result: {res}")
    return checker

@checker


def calculate(expression):
    return eval(expression)


calculate = checker(calculate)
calculate(input("введіть вираз "))
