import time

def time_check(function):
    def time_check1(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        a = end - start
        print(f"час {a} ")
        return end - start
    return time_check1

def one():
    for i in range(1, 100001):
        print(i)

decor = time_check(one)
result =decor()


