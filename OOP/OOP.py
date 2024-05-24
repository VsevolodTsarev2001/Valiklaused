class Student:

    s = Student()
    print(type(s))  # <class '__main__.Student'>
    print(id(s))    # 12448112

    t = Student()
    print(type(t))  # <class '__main__.Student'>
    print(id(t))    # 12423408

    def greet_friend(self, friend_name):
        print(f"Hello, {friend_name}")

    s = Student()
    s.greet_friend("Kaia")


        def __init__ (self, name, title, age):
            self.name
            self.title
            self.age
        def hello(Self):
            print(self.name)


        def hello(self):  # method, "self" is a special parameter
            """Method (function) which just prints out "Hello!"."""
            print("Hello!")


    s = Student()   # s is an object of class Student
    s.hello()       # no "self" argument


    def __init__(self, name, title):
        self.name = name
        self.title = title

ago = Student("Ago", "Sir")
print(ago.name)

leela = Student("Leela", "Captain")
print(leela.title)

    def __init__ (self):
        print("Initializing student..")

s = Student()  # Initializing student

class Student:
    def __init__(self, name, title):
        self.name = name
        self.title = title 
    def  hello(self):
        print(self.name)
    def upgrade(self):
        self.title +="!"
s=Student("ago","Feacher")
print(S.name)
s.hello)


