class A:
    def say_hello(self):
        print("Hello from class A")

class B(A):
    def say_hello(self):
        super().say_hello()
        print("Hello from class B")

class C(B):
    def say_hello(self):
        super().say_hello()
        print("Hello from class C")
        

objc = C()
objc.say_hello()