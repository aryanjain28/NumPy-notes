import numpy

OneDArray = numpy.array([1,2,3])
# print(OneDArray)

TwoDArray = numpy.array([['a','b','c'], ['d','e','f']])
# print(TwoDArray)

ThreeDArray = numpy.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
# print(ThreeDArray)

#changing datatypes :
dataType = numpy.dtype([('name', 'S20'), ('age', '>i1'), ('marks', '>f4')])
# print(dataType)
#each element is a data type that contains a name age and marks
myArray = numpy.array([[('Aryan', 20, 78.98), ('Roushan', 19, 87.76), ('Aayush', 19, 97)],
                       [('Vipul', 20, 79.68), ('Nikhil', 19, 47.76), ('Naman', 19, 99)]],
                      dataType)
#print(myArray)

import random

alphabets = list('qwertyuiopasdfghjklzxcvbnm')
# print(alphabets)

myArray0 = []
[myArray0.append(alphabets[random.randrange(0, 26)]) for _ in range(30)]
myArray0 = numpy.array(myArray0)
# print(myArray0)

#1-D
# print(myArray0.shape)

#Converting to 2-D
myArray0 = myArray0.reshape(6,5)
# print(myArray0)

#Converting to 3-D
myArray0 = myArray0.reshape(3,5,2)
# print(myArray0)

# size of each item
# print(myArray0.itemsize)

