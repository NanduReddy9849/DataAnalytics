import numpy as np
arr=np.array([1,2,3])
print(arr)
print(type(arr))

print(np.zeros((2,3)))
print(np.ones((3,2)))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))
print(np.random.rand(2,2))


# Example

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)
print(a**2)
print(a/b)
print(np.sqrt(a))

# Example

A=np.array([[1,2],[3,4]])
B=np.array([[2,0],[1,3]])

print(np.dot(A,B))
print(np.transpose(A))
print(np.linalg.inv(A))

# Example

arr=np.array([1,2,3,4])
print(arr.mean())
print(arr.sum())
print(arr.std())  # standard deviation
print(arr.max())
print(arr.min())