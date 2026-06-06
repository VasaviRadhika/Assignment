class Person:
    def getGender(self):
        return "unknown"
class Male(Person):
    def getGender(self):
        return "male"
class Female(Male):
    def getGender(self):
        return "female"
p=Person()
m=Male()
f=Female()
print(p.getGender())
print(m.getGender())
print(f.getGender())
