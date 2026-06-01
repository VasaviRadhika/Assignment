#3.movie ticket pricing
Age=int(input("Enter your age"))
print("---Ticket Booking--- ")
if Age<=5:
  category="infant"
  ticket_price="free"
elif Age>5  and Age<=12:
  category="Child"
  ticket_price='100'
elif Age>13 and Age<=59:
    category="adult"
    ticket_price='250'
else:
    category="senior citizen"
    ticket_price='150(senior citizen)'
print(f"Age:{Age}")
print(f"Category:{category}")
print(f"Ticket Price:{ticket_price}")

