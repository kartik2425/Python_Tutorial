av=5

x=int(input("How candles you want"))

i=1
while i<=x :
    if i>av:
        print("out of stock")
        break

    print(i,"candles")
    i+=1