from array import *
vals=array('i',[5,-9,3,4,2])
print(vals.buffer_info())#to find address and size
print(vals.typecode)#to find the type of code
print(type(vals))#type of data type
vals.reverse()#reverese the array
print(vals[4])
for i in range(len(vals)): #print the value one by one 
    print(vals[i])
