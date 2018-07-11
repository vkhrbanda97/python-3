def modulus(a,b):
  if a<0:
    return modulus(a+b,b)
  elif a<b:
    return a
  else:
    return modulus(a-b,b)


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The modulus is",modulus(a,b))