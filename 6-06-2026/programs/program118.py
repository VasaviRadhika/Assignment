def budget(lst):
    total=sum(person['budget'] for person in lst)
    return total
user=[]
num=int(input("how many peoples to add: "))
for i in range(num):
    name=input("enter your name: ")
    age=int(input("enter your age: "))
    amount=int(input("enter your budget: "))
    user.append({'name':name,'age':age,'budget':amount})
result=budget(user)
print("total budget is: ",result)
    
    
