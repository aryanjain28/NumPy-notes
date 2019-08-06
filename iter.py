import numpy

a = numpy.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(a)
print("\n")

#Iterationg througn each element in a:
[print(x, end=" ") for x in numpy.nditer(a)]
print("\n")

#ITranspose of a :
b = a.T
print(b)
print("\n")

#Iterationg througn each element in b: (same as a because it iterates through memory ordering : )
[print(x, end=" ") for x in numpy.nditer(b)]
print("\n")

print("\nOriginal matrix : ")
print(a)

print("\n\nC-style : ")
[print(x, end=" ") for x in numpy.nditer(a, order='C')]     #Column style
print("\n\nF-style : ")
[print(x, end=" ") for x in numpy.nditer(a, order='F')]     #Row style


#MODIFYING ARRAY VALUES :
print("\n\nOriginal array : \n")
print(a)
print("\n")
for x in numpy.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x

print("\n\nModified array : \n")
print(a)
