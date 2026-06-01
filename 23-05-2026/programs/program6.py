pin=1234
userpin=int(input("enter user pin: "))
balance=5000
if pin==userpin:
    withdraw=int(input("enter withdraw amount: "))
    if balance>withdraw:
         print(f"balance available:{balance-withdraw}")
    else:
        print("balance not available")
else:
    print("incorrect pin")
