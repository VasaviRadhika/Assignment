def username(email):
    parts=email.split('@')
    if len(parts)==2:
        return parts[0]
    else:
        return "invalid format"
try:
    mail=input("enter your email: ")
    un=username(mail)
    print(un)
except ValueError:
    print("invalid input")
