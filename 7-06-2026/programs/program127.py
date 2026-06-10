def symmetric(num):
    num_str=str(num)
    return num_str==num_str[::-1]
print(symmetric("1234567"))
print(symmetric("123321"))
