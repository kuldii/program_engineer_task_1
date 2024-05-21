def foo(a, b):
    print("Value of a:", a)
    print("Value of b:", b)


def bar():
    if True:
        print("True")
    else:
        print("False")


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello, my name is ' + self.name)
