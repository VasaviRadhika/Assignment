#A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
n=int(input("enter a number:"))
sum=0
while n>0:
    sum= sum+n%10
    n=n//10
print(sum)
if n%sum==0:
    print( " the given number is a harshad number")
else:
    print("the given number is not a harshad number")
