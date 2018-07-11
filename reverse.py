print("The reverse of a given nuber")
print("")
n=int(input("Enter any number:"))
r=0
while n>0:
  b=n%10
  r=r*10+b
  n=n//10

print("The reverse of a number is :",r)  