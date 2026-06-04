class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck(Flyer, Swimmer): 
    pass
a1=Duck()
print(a1.fly())
print(a1.swim())
