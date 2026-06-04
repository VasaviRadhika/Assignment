class Animal:
    def cat(self):
        return "meow meow"
class Birds(Animal):
    def crow(self):
        return "kwa kwa"
a1=Animal()
a2=Birds()
print(a1.cat())
print(a2.crow())
    
