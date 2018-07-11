x=10
x=int(x)
print(x)
print(type(x))
print(type(x)==int)
print(id(x))

x=2.6
x=float(2.6)
print(x)
print(type(x)==float)
print(id(x))

x=4+3j
x=complex(4+3j)
print(x)
print(type(x))
print(type(x)==complex)
print(id(x))

x="Vishal"
y='Single'
z="""MULTI
line"""
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
print(type(x)==str)
print(type(y)==str)
print(type(z)==str)
print(id(x))

x=[1,2,3,"PY"]
x=list([1,2,3,"PY"])
print(x)
print(type(x))
print(type(x)==list)
print(id(x))

x=(1,2,3,"PY")
x=tuple((1,2,3,"PY"))
print(x)
print(type(x)==tuple)
print(id(x))

x={1:"Python",2:"Java"}
x=dict({1:"Python",2:"Java",3:"Python"})
print(x)
print(type(x))
print(type(x)==dict)
print(id(x))

x={10,"Python",20}
x=set({10,"Python",20})
print(x)
print(type(x))
print(type(x)==set)
print(id(x))

