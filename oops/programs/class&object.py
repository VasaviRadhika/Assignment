class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def description(self):
        print(f"year:{self.year}\n make:{self.make}\n model:{self.model}\n")
c1=Car("Honda","civic",2023)
c2=Car("Toyota","coralla",2022)
c1.description()
c2.description()
