def myfun(n):
    return lambda a:a*n
m=myfun(3)
n=myfun(4)
print(m(2))
print(n(6))