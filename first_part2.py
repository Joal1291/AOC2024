import openfile
import re

puzzle = openfile.readFile("first.txt")

left_list = []
right_list = []

result = 0

for line in puzzle:
    x, y = map(int, re.findall(r"\d+", line))
    left_list.append(x)
    right_list.append(y)

for int in left_list:
    multiply = right_list.count(int)
    result+= multiply*int

print(result)