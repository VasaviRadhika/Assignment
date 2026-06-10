def words(input):
    sort_dict=sorted(input.items())
    result=[(key,value) for key,value in sort_dict]
    return result
print(words({"D": 1, "B": 2, "C": 3}))
