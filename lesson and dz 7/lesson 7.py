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

res = num_to_degrees(int(input("num - ")), int(input("degree - ")))
print(next(res))

for num in res:
    print(num)