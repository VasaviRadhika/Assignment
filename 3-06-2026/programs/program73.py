dictionary={'apple':2,'mango':1,'banana':12}
a=dict(sorted(dictionary.items()))
for key,value in a.items():
    print(f"{key}:{value}")
