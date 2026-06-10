def ci(p,t,r,n):
    a=p*(1+(r/n))**(n*t)
    return round(a,2)
print(ci(10000,10,0.5,12))
