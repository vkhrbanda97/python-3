print("TO find the LCM and GCD of the two numbers")
print("")

while True:

  print("1.GCD")
  print("2.LCM")
  print("3.Exit")

  choice=int(input("Enter the choice"))

  if choice==1:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if a>b:
      small=b
    else:
      small=a
    for x in range(1,small+1):
      if((a%x==0) and (b%x==0)):
        gcd=x  
    print("The GCD of the number is:", gcd)    

  if choice==2:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if a>b:
      small=b
    else:
      small=a
    for x in range(1,small+1):
      if((a%x==0) and (b%x==0)):
        gcd=x
    lcm=(a*b)//gcd
    print("The LCM of the given number is:", lcm)      

  if choice==3:
     break