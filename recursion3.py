def div(m,n):

  if m<n:
    return 0
  else:
    return div(m-n,n)+1  







m=int(input("Enter the number :"))
n=int(input("Enter the number:")) 
print("The division is ",div(m,n))