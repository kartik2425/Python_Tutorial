nums=[12,25,22,43,23,2]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")