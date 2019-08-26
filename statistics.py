import numpy

a = numpy.array([[1,2,3,4],[6,1,6,6],[8,3,5,1],[4,5,7,3],[6,2,1,1]])
print("\nOriginal array : ")
print(a)

print("\nGetting the minimum in complete matrix : ")
print(numpy.amin(a))

print("\nGetting the minimum a/c to axis : ")
print(numpy.amin(a, 0))     #vertical
print(numpy.amin(a, 1))     #horozontal

print("\nGetting the maximun a/c to axis : ")
print(numpy.amax(a, 0))     #vertical
print(numpy.amax(a, 1))     #horozontal

print("\nGetting a range between maximum and minimum : ")
print(numpy.ptp(a))     #max-min : 8-1 = 7

#ptp == peek to peek

print("\nGetting a range between maximum and minimum a/c to axis: ")
print(numpy.ptp(a, 0))

print("\nGetting a range between maximum and minimum a/c to axis: ")
print(numpy.ptp(a, 1))

print("\nNew matrix : ")
x = numpy.array([[56,43,32],[73,56,57],[16,73,27]])
print(x)

print("\nGetting complete matrix's percentile : ")
print(numpy.percentile(x, 10))

print("\nGetting percentile a/c to axis 0 : ")
print(numpy.percentile(x, 50, 0))

print("\nGetting percentile a/c to axis 1 : ")
print(numpy.percentile(x, 50, 1))

print("\n")
p = []
[p.append(int(x)) for x in numpy.nditer(a)]
print(sorted(p))
print("\n")

print("\nGetting median of complete array : ")
print(numpy.median(a))

print("\nGetting median a/c to axis 0 : ")
print(numpy.median(a, 0))

print("\nGetting median a/c to axis 0 : ")
print(numpy.median(a, 1))

print("\n")
print(a)

print("\nGetting mean of complete array : ")
print(numpy.mean(a))

print("\nGetting mean of a/c to axis 0 : ")
print(numpy.mean(a, 0))

print("\nGetting mean of a/c to axis 0 : ")
print(numpy.mean(a, 1))


print("\nGetting average : ")
print(numpy.average(a))

print("\nGetting average a/c to axis 0 : ")
print(numpy.average(a, axis=0))

print("\nGetting average a/c to axis 1 : ")
print(numpy.average(a, axis=1))

print("\n")
print(a)

print("\nGetting complete average : ")
print(numpy.average(a))

print("\nGetting average a/c to axis 0: ")
print(numpy.average(a, axis=0))

print("\nGetting average a/c to axis 1: ")
print(numpy.average(a, axis=1))

print("\n")
print(a)

wt = numpy.array([4,3,2,1,0])

print("\nGetting average with weights with axis 0 : ")
print(numpy.average(a, weights=wt, axis=0))

wt = numpy.array([1,2,3,4])

print("\nGetting average with weights with axis 1 : ")
print(numpy.average(a, weights=wt, axis=1))

print("\nSetting weights for each row : ")
wt = numpy.array([[1,2,3,4],[6,3,6,0],[3,6,7,8],[6,2,7,1],[6,2,7,1]])
print(numpy.average(a, weights=wt, axis=1))

print("\nGetting standard deviation of array : ")
print(numpy.std(a, axis=1))

print("\nGetting variance of array : ")
print(numpy.var(a, axis=1))
