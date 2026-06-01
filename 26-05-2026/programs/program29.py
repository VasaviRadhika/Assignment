weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
bmi=weight/height**2
if bmi<=18.5:
    print("under weight")
elif bmi>18.5 and bmi<=24:
    print("normal")
elif bmi>24 and bmi<=29:
    print("over weight")
else:
    print("obese")

