list1=["a","b","c"]
list2=[1,2,3,4]
list3=list1+list2
print("joing a two list")
print(list3)
print("printing a extend list")
list1.extend(list2)
print(list1)
list3.extend(list1)
print(list3)