from collections import OrderedDict
def check(string,reference):
     string_dict = OrderedDict.fromkeys(string)
     reference_dict = OrderedDict.fromkeys(reference)
     return string_dict==reference_dict
input1=input("enter the words")
input2=input("enter the words")
if check(input1,input2):
    print("the characters are matching in both strings")
else:
    print("the characters are not matching in the strings")
