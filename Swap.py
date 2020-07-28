#different way swaping
print("using temp variable")
a=5
b=6
temp=a
a=b
b=temp
print(a)
print(b)
print("using arithmatic operators")
x=6
y=5
x=x+y
y=x-y
x=x-y
print(x)
print(y)
print("within one line swaping")
a=8
b=9
a,b=b,a
print(a)
print(b)
print("using xor to swap")
x=10
y=15
x=x^y
y=x^y
x=x^y
print(x)
print(y)
