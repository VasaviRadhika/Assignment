def remove(input,i):
    if i<0 or i>=len(input):
        print(i,"the value is not valid")
        return input
    result=input[:i]+input[i+1:]
    return result
input="vasavi radhika"
i=9
new_str=remove(input,i)
print("original string:",input)
print(f"string after removing{i}th character:{new_str}")
