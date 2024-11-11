from lib2to3.fixes.fix_print import parend_expr
import numpy as np

a= np.array([1,2,3])
print(a.ndim)
print(a)
a= np.array([1,2,3], dtype=float)
print(a)

b= np.array([[1,2,3], [4,5,6]])
print(b.ndim)
print(b.dtype)
#Access elements
print(b[0,2] )
#Get a specific column
print(b[:,0])
b[0,2] = 100
print(b)

print(np.zeros((3,3), dtype=np.int64))

print(np.full((3,3),50, dtype=np.int64))
#Randomn array
np.random.rand(4,4)

np.random.randint(-4,1, size=(3,3))
print(np.identity(3))

a= np.array([[1,2,3,4,5,6],
             [10,20,30,40,50,60],
             [12,12,12,12,12,12],
             [11,21,31  ,41,51,61],
             [13,24,34,44,54,64]])

print(a[:3,-5:])

# Create an (nxn) array with all zeros
#z = np.zeros((n,n), dtype=np.int64)
#print(z)
# Make the middle row and column all 1s

#z[n//2,:] = 1
#z[:,n//2] = 1

# Print the final value of z
#print(z)

a= np.array([1,2,3])
print(a+2)
print(a)
a.min()
np.min(a)
print(a.mean())
print(np.sum(a))
print(a.sum())
    
