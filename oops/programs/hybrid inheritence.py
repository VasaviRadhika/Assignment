class A:
    def a(self):
        return "A"

class B(A):
    def b(self):
        return "B"

class C(A):
    def c(self):
        return "C"

class D(B, C):  
    pass
d=D()
print(d.b())
print(d.c())
print(d.a())


