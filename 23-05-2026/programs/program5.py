#5.student grade calculator
marks=int(input("Enter Marks"))

if marks>=90:
    Grade='S'
    Result="pass"
elif marks>=80:
     Grade='A'
     Result="pass"
elif marks>=70:
    Grade='B'
    Result="pass"
elif marks>=60:
    Grade='C'
    Result="pass"
elif marks>=50:
    Grade='D'
    Result="pass"
else:
    Grade=''
    Result="Fail"
print("---Result---")
print(f"Marks:{marks}")
print(f"Grade:{Grade}")
print(f"Result:{Result}")
