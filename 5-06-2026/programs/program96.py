def binary(decimal):
    st=""
    while decimal>0:
        rem=decimal%2
        st=str(rem)+st
        decimal=decimal//2
    return st if st else "0"
print(binary(1))
print(binary(2))
