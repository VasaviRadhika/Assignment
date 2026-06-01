#4.employee bonus calculator
salary=int(input("enter your salary: "))
experience=int(input("enter your experience: "))
if experience>10:
    percentage=20
    bonus=percentage*salary
    takehome=bonus+salary
elif experience>5 and experience<=10:
    percentage=15
    bonus=percentage*salary
    takehome=bonus+salary
elif experience>2 and experience<=5:
    percentage=10
    bonus=percentage*salary
    takehome=bonus+salary
else:
    percentage=0
    bonus=percentage*salary
    takehome= bonus+salary
print("---Bonus Details---")
print(f"Salary :{salary}")
print(f"Experience:{experience}")
print(f"Bonus  : {percentage}%  (₹{bonus})")
print(f"Take Home:{takehome}")
