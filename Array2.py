from array import *

arr=array('i',[])

n=int(input("Enter the size of a array"))

for  i in range(n):
    x=int(input("enter the values"))
    arr.append(x)

print(arr)

val=int(input("enter the value for search"))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))

