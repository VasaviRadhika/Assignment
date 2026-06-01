#1.income tax calculator
salary=float(input())
print("---Tax Summary---")
print(f"annual salary:{salary}")
if salary>1500000:
    print("Tax rate:30%, ({tax})")
    tax=(30*salary)/100
    print(f"net salary:{salary-tax}")
elif salary>1000000:
    print("Tax rate:20%,({tax:.2f})")
    tax=(20*salary)/100
    print(f"net salary:{salary-tax}")
elif salary>500000:
    print("Tax rate:10% ({tax})")
    tax=(10*salary)/100
    print(f"net salary:{salary-tax}")
elif salary<=500000:
    print("no tax")
    print(f"net salary :{salary}")
