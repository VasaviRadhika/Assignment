class Divisible_seven:
    def __init__(self,n):
        self.n=n
    def genarate(self):
        for num in range(self.n+1):
            if num%7==0:
                yield num
n=int(input("enter the range:"))
divisibility=Divisible_seven(n)
for num in divisibility.genarate():
    print(num)
