def line(lst,n):
    if lst:
        lst.pop(0)
        lst.append(n)
        return lst
    else:
        return "no list has been selected"
print(line([1,2,3,4,5],10))
