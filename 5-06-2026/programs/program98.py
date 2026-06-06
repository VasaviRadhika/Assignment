def signs(expression):
    try:
        return eval(expression)
    except:
        return False
print(signs("4<7<2"))
