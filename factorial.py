print("To print the Factorial of a number ")
print("")
f=1

num=int(input("Enter the number :"))


if num<0:
  print("The factorial of negative number does not exist!!!")
elif num==0:
  print("The factorial of 0 is always 1")
else:
  while num>0:
    f=num*f
    num-=1    
  print("The factorial is",f)