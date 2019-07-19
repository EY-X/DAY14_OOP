class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'Hi my name is {self.name}'

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def learn(self):
        return 'I get it!'

class Instructor(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        return 'An object is an instance of a class'






        

instance1 = Instructor('Nadia')
# print(instance1.greeting())

instance2 = Student('Chris')
# print(instance2.greeting())

print(instance1.learn())

# INSTANCE1 IS ASSIGNED TO THE INSTUCTOR CLASS
# INSTANCE2 IS ASSIGNED TO THE STUDENT CLASS

