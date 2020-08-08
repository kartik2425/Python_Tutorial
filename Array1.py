from array import *

vals=array('i',[5,8,9,4,3])

newArray=array(vals.typecode,(a*a  for a in vals))

i=0

for e in newArray:
    print(e)

#using while loop
'''  i=0
while i<len(newArray):
print(newArray(i))
i+=1
'''