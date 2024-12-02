import re
import openfile

puzzle = openfile.readFile("first.txt")

array_1= []
array_2= []

for i in puzzle:
    o = i.split("   ")
    array_1.append(int(o[0]))
    array_2.append(int(o[1]))

b = sorted(array_1)
c = sorted(array_2)

array_3 = []

for a, b in zip(b, c):
    if a > b:
        array_3.append(a - b)
    elif a < b:
        array_3.append(b - a)
    else:
        array_3.append(0)

print(sum(array_3))