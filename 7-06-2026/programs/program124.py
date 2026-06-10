def society(names):
    secret=''.join(sorted([name[0] for name in names]))
    return secret
print(society(["vasavi","vineela","anitha","nageswararao"]))
