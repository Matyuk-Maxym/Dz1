list_car = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for car in list_car:
    if car == "eight":
        continue
    # print(car)


iterator = iter(list_car)

# print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("===============================")
for car in iterator:
    print(car)

# stopiteration
# print(next(iterator))


class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number


    def __iter__(self):
        self.i = 0
        return self


    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
counter = Counter(5)

# for count in counter:
#     print(count)

print("=================================")
print(counter.__next__())
print(counter.__next__())
print(counter.__iter__())
print(next(counter))
print(next(counter))
print(next(counter))

print("======== genErator ========")
# ======== generator ========

def num_to_degrees(number, max_degree):
    i = 0
    for deg in range(max_degree):
        yield number**i
        i += 1

def number_to_degrees(number):
    i = 0
    while True:
       result = number**i
       yield result
       if result > number ** 5:
           return
       i += 1




res = num_to_degrees(int(input("num - ")), int(input("degree - ")))
print(next(res))

for num in res:
    print(num)

print("-------------")

res = number_to_degrees(10)


for num in res:
    print(num)

# замикання функцій
print("=============замикання функцій===========")

class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"Self = {self.work}, no self = {work}"

helper = Helper("Classwork")
print(helper("homework"))

# ========== decorators ===============
print("========== decorators ===============")

