#creating own function like print()

def greet():  #defining a statement
    print("hello")
    print("Good morning")

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(5,4)  # we can run using single result variable  we get same output
print(result1,result2)
greet()

