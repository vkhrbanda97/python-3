print("To print whether the number is armstrong or not ")
print("")

n=int(input("Enter a number:"))
t=n
s=0
while t>0:
  dig=t%10
  s+=dig**3
  t//=10
if n==s:
  print("the number is armstrong")
else:
  print("the number is not armstrong")