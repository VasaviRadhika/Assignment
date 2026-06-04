import re

def is_valid_password(password):
   password=password.strip()
   if 6 <= len(password) <= 12:
      if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}", password):
          return True
   return False

passwords = input("Enter passwords separated by commas: ").split(',')
valid_passwords = []
for psw in passwords:
   if is_valid_password(psw):
     valid_passwords.append(psw)
print(','.join(valid_passwords))
