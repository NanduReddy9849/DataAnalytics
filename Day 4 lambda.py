""" lambda Function """

s1="Hello Good Morning"
s2=lambda func:func.upper()
print(s2(s1))


n=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print(n(5))
print(n(-3))
print(n(0))


sq = lambda x:x**2
print(sq(5))

li=[lambda arg=x: arg * 10 for x in range(1,5)]
for i in li:
    print(i())
    
check = lambda x:"Even" if x%2==0 else "odd"
print(check(4))
print(check(7))


""" Lambda with Multiple statements """

calc=lambda x,y:(x+y,x*y)
res=calc(3,4)
print(res)    #returns in a tuple


n=[1,2,3,4,5]
even=filter(lambda x:x%2==0,n)
print(list(even))

a=[1,2,3,4]
b=map(lambda x: x*2,a) #map() iterates through a and applies the transformation(x*2)
print(list(b))


from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y:x*y,a) # x=1*y=2==>2 ; x=2 y=3==>6 ; x=6 y=4 ==>24
print(b)
