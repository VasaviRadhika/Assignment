
my_dict={
    'a':1,
    'b':1,
    'c':2,
    'd':3,
    'e':4
}
uni_val=set()
for i in my_dict.values():
    uni_val.add(i)
unique=list(uni_val)
print(unique)
                      
