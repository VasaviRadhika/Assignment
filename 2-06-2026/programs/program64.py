def uncomman_words(str1,str2):
    word1=set(str1.split())
    word2=set(str2.split())
    uncomman_set=word1.symmetric_difference(word2)
    uncomman_list=list(uncomman_set)
    return uncomman_list
string1=input()
string2=input()
uncomman=uncomman_words(string1,string2)
print("uncomman words:",uncomman)
