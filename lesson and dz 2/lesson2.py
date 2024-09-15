class Student:
    count = 0
    def __init__(self, name, age = 18, height = 170):
        self.height = height
        self.name = name
        self.age = age
        Student.count += 1

    def show(self):
        print("============================")
        print("Ім'я = ", self.name)
        print("Вік = ", self.age)
        print("Зріст = ", self.height)
        print("count = ", self.count)
        #print(self)

    def __str__(self):
        return "Hello, my name is " + self.name + "!"

jack_student = Student("Jack", 15, 160)
kirill_student = Student("Kiril", 14, 165)
bob_student = Student("Bob")
#print("============================")
#print("Ім'я = ", jack_student.name)
#print("Вік = ", jack_student.age)
#print("Зріст = ", jack_student.height)
#print("count = ",jack_student.count)
#print("============================")
#print("Ім'я = ", kirill_student.name)
#print("Вік = ", kirill_student.age)
#print("Зріст = ", kirill_student.height)
#print("count = ",kirill_student.count)
#print("============================")
#print("Ім'я = ", bob_student.name)
#print("Вік = ", bob_student.age)
#print("Зріст = ", bob_student.height)
#print("count = ",bob_student.count)
#print("============================")

jack_student.show()
kirill_student.show()
bob_student.show()

print(jack_student)
print(kirill_student)
print(bob_student)
