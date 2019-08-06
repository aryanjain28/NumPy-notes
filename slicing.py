import numpy

a = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print("Our array is : \n")
print(a)
print("\n")

print("Printing all from 1 row onwards : ")
print(a[1:])
print("\n")

print("Printing all from 1 row to 2 row : ")
print(a[0:2])
print("\n")

print("Printing all with a skip of 2 : ")
print(a[::2])
print("\n")

print("Printing all : ")
print(a[::])
print("\n")

print("Accessing elements 4 and 6 : ")
print(a[1:2:][0][0::2])
print("\n")

#Using ellipsis :

print("Print elememts in 1 column : ")
print(a[...,1])
print("\n")

print("Print elememts from 1 column onwards : ")
print(a[...,1:])
print("\n")

print("Print elememts from 0 column onwards with a skip of 2 : ")
print(a[...,0::2])
print("\n")

#similarly for rows :

print("Print 2 row elememts : ")
print(a[1:2:,...])
print("\n")

print("Print 1 and 3 row elememts : ")
print(a[0::2,...])
print("\n")

#Applications :
print("Printing all corner elements : ")
print(a[::2,...][...,::2])
print("\n")



#ADVANCED INDEXING :

x = numpy.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x)
print("\n")

#CASE 1:
print("Printing corner elements in a single line : \n")
print(x[[0,0,3,3],[0,2,0,2]])
print("\n")

#CASE 2:
print("Printing corner elements in matrix form : \n")
print(x[[[0,0],[3,3]],[[0,2],[0,2]]])
print("\n")

#CASE 3:
print("Using ::")
print(x[1:4, 1:3])     #each and every element between (1,2,3) and (1,2)
print("\n")

#CASE 4:
print(x[1:4, [2]])      #each and every element between (1,2,3) and (2)
print("\n")

#Boolena indexing :
print(x[x > 5])     #print elements that are greater than 5
print("\n")

c = numpy.array([1+2j, 3, 4, 5+9j, 6, 9+7j])
print(c[numpy.iscomplex(c)])        #print all that are complex
print(c[~numpy.iscomplex(c)])        #print all that are NOT complex
