""" Exception Hnadling Errors """


""" NameError """

try:
    print(x)
except NameError:
    print("the Variable x is not defined !")
except:
    print("please check the logic !")
finally:
    print("I am always executed")


""" Type Error """

x=10
y="hello"
try:
    print(x+y) #TypeError
except NameError:
    print("The variable x is not defined")
except TypeError:
    print("x and y are not strings")
except:
    print("please check the logic")
finally:
    print("I am always Executed")
    
    
""" Value Error """

try:
    x=int(input("x:"))
    y=int(input("y:"))
    print(x+y)
except NameError:
    print("the variable x is not defined")
except TypeError:
    print("x and y are not strings")
except ValueError:
    print("please give always x and y as integer")
except:
    print("please check the logic")
finally:
    print("I am always executed")
    
    
    
""" IndexError """

try:
    l1=[1,2,3,4,5,6,7]
    print(l1[10])
except NameError:
    print("the variable x is not defined")
except TypeError:
    print("x and y are not strings")
except ValueError:
    print("please give always x and y as integer")
except IndexError:
    print("please check the index is given")
finally:
    print("I am always executed")
    

""" KeyError """

try:
    d1={1:2,3:4,5:6}
    print(d1[100])
except IndexError:
    print("please check the index is given")
except KeyError:
    print("given key is not found in the dictionary")
except:
    print("please check the logic once !")
finally:
    print("I am always executed")


""" FileNotFoundError """

try:
    fp=open("sample333.txt","r")
    print(fp.read())
except IndexError:
    print("please check the index is given")
except KeyError:
    print("given key is not found in the dictionary")
except FileNotFoundError:
    print("give file is not found !")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")
    
    
""" ModuleNotFoundError """

try:
    import Sample33
except FileNotFoundError:
    print("give file is not found")
except ModuleNotFoundError:
    print("given module is not found")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")
    
    
""" AttributeError """

try:
    import math
    print(math.sqqrt(20))
except FileNotFoundError:
    print("give file is not found")
except ModuleNotFoundError:
    print("given module is not found")
except AttributeError:
    print("given method is not found")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")


""" SyntaxError """

try:
    global x = 100   # Error
except SyntaxError:
    print("do not assign value when we using global keyword")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")


""" Arithmetic Error """

a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")


""" OverflowError """

import math as mt
try:
    print(mt.factorial(30))
    print(mt.exp(10000))
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except OverflowError:
    print("please give the power value minimum")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")
    

""" OSError """

import os
try:
    os.remove("sample444.txt")
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except OSError:
    print("please check the  given file is there or not")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")
    
    
""" RecursionError """

import os
try:
    def display():
        display()
    display()
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except RecursionError:
    print("recursion will reach its's maximum depth")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")


""" UnBoundLocalError """

try:
    def display():
        a1=10
        def display2():
            nonlocal a
            a=100
            print(a)
        display2()
    display()
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except UnboundLocalError:
    print("print after the value assignment ")
except:
    print("please check the given logic once !")
finally:
    print("I am always executed")
        
    
""" StopIteration """

try:
    i1=iter([10,20,30,40])
    print(next(i1))
    print(next(i1))
    print(next(i1))
    print(next(i1))
    print(next(i1))
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except SyntaxError:
    print("print after the value assignment ")
except StopIteration:
    print("please check the given logic once !")
finally:
    print("I am always executed")


""" KeyboardInterrupt """

try:
    a=int(input("a:"))
except ZeroDivisionError:
    print("do not divide the numberb with zero")
except SyntaxError:
    print("print after the value assignment ")
except KeyboardInterrupt:
    print("please check the given logic once !")
finally:
    print("I am always executed")
    
