#2.electricity bill calculator
units=int(input("enter units"))
if units>300:
  Rate_applied=6
elif units>200:
  Rate_applied=4
elif units>100:
  Rate_applied=3
elif units>0:
  Rate_applied=2
print("---Electricity Bill---")
print(f"Units consumed {units}")
print(f"Rate Applied {Rate_applied}")
print(f"Total Bill:{units*Rate_applied}")


