defmul(m,n):
if(n>0):
print(m,n)

returnm+mul(m,n-1) 

else:
return0





m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print("The multiplication is",mul(m,n))
