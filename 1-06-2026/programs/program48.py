#pronic number
#𝑃 = 𝑛 ∗ (𝑛 + 1) 𝑛

def pronic(num):
    for n in range(1,int(num**0.5)+1):
        if n*(n+1)==num:
            return True
    return False
print("pronic numbers between 1 and 100 are:")
for i in range(1,101):
    if pronic(i):
        print(i,end=",")
    
