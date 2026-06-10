def reverse(value):
    if isinstance(value,bool):
        return not value
    else:
        return "boolean values are only accepted"
print(reverse(True))
print(reverse(False))
print(reverse("vf"))
