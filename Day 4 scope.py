""" Scope """

# local scope

def myfunc():
    x=300
    print(x)
    
myfunc()


# Enclosing scope

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
    
myfunc()

# Global scope

x=300
def myfunc():
    print(x)
myfunc()
print(x)
