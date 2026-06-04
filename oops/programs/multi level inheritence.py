class Living:
    pass
class Plant(Living):
    pass
class Flower(Plant):
    def name(self):
        return "lilly"
a1=Flower()
print(a1.name())
    
