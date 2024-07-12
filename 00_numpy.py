import numpy as np
import logging 
logging.basicConfig(filename="00_logging.log",level=logging.DEBUG)
# one diamensional array
myarr=np.array([4,56,57,34,97,34], np.int64)
logging.info(myarr)
logging.info("TYPE:{}".format(myarr.dtype))
logging.info(type(myarr))
#two diamensional array
myarr1=np.array([[1,2,3,4,5]])
logging.info(myarr1[0])
logging.info(myarr1.shape)
logging.info(myarr1[0,1])

# changing the value of an element
logging.info("old array={}".format(myarr1))
myarr1[0,2]=69
logging.info("new array={}".format(myarr1))


# array creation using other python structures
listarray=np.array([[1,2,3],[5,6,3],[6,7,8]])

# zeroes array creation 
zeros=np.zeros((3,3))
logging.info(zeros)

#range array
rng=np.arange(15)
logging.info("range array:{}".format(rng))

# create a linearly spaced array np.linspace(<start>,<end>,<number of elements>)
lspace=np.linspace(1,10,10)
logging.info("linearly spaced array:{}".format(lspace))

# creating an empty array (stores random values which can be updated)
emp=np.empty((1,2))
logging.info("Empty array:{}".format(emp))

# creating an array which stores data similar to previous array 
emp_like=np.empty_like(lspace)
logging.info("Empty like array".format(emp_like))

# identity matrix array 
ide=np.identity(45) #always returns a two diamensional array like square matrix.
logging.info("Identity array:{}".format(ide))

# reshaping an array
arr=np.arange(50)
logging.info("Sample array={}".format(arr))
arr=arr.reshape(2,25) #note that the number of elements must be same 
logging.info("Reshaped array:{}".format(arr))

#to convert a two diamensional array into one diamensional:

logging.info("Sample array={}".format(arr))
arr=arr.ravel()
logging.info("Converted array:{}".format(arr))

#attributes
# numpy axis : one diamensional array has one axis(axis0) and a two diamensional array has two axis(axis0,axis1)
# converting a list to array:
x=[[1,2,3],[4,5,6],[7,8,9]]
x=np.array(x)

#to get the sum of columns, use array.sum(axis=0)
y=x.sum(axis=0)
logging.info("Sum of columns:{}".format(y))

#to get the sum of rows, use array.sum(axis=1)
z=x.sum(axis=1)
logging.info("Sum of rows:{}".format(z))

sample=[[1,2,3],[4,5,6],[7,8,9]]
sample=np.array(sample)
logging.info("Sample array:{}".format(sample))

# to create an iterator, use array.flat

r=sample.flat
logging.info("elements:")
for item in r:
    logging.info(item) #this prints all the elements in an array

#to transpose a matrix array, use array.T
a=sample.T
logging.info("Transposed array:{}".format(a))

#to find the number of diamensions in an array use array.ndim
d=sample.ndim
logging.info("Number of diamensions:{}".format(d))

#to find the number of elements, use array.size
s=sample.size
logging.info("Size of array:{}".format(s))

#to find the number of bytes consumed by an array, use array.nbytes
b=sample.nbytes
logging.info("Number of bytes used:{}".format(b))

#methods 
#to directly get the element and not the index of it , remove arg from the arguments, e.g. array.argmax will become array.max()
max=sample.argmax() #returns the index of greatest element in the array
logging.info("Index of max element:{}".format(max))

min=sample.argmin() #returns the index of smallest element in the array
logging.info("Index of min element:{}".format(min))

sort=sample.argsort() #sorts the indexes of a given array in ascending order
logging.info("Sorted indexes :{}".format(sort))

#to perform these actions row wise or column wise, give argument o axis in the function paranthesis

#mathematical matrix operations 
sample2=[[3,4,2],[8,6,2],[7,3,9]]
sample2=np.array(sample2)

sum=sample+sample2 #adds two array in matrix method
logging.info("Sum of the arrays:{}".format(sum))

prod=sample*sample2 #multiplies two arrays in matrix method
logging.info("Product of the arrays:{}".format(prod))

sqroot=np.sqrt(sample) #stores square-root of each element in its place as an array
logging.info("Square-root of the given matrix={}".format(sqroot))

# search an element
found=np.where(sample>4) #returns in a tuple format
logging.info("Index of all elements that satisfy the fiven condition:{}".format(found))

# to find the total number of non zero elements in an array use np.count nonzero(array)
num=np.count_nonzero(sample)
logging.info("Number of non-zero elements={}".format(num))



