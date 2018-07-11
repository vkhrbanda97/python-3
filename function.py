def fact(n):

print("ITERATIVE CALL: ",n )

prod = 1

for x inrange(1,n+1):
prod *= x

return prod

n = int(input("ENTER N:") )

print("FACT(N): " + str( fact(n) ))
