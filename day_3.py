import re
import openfile

puzzle = openfile.brutFile('day_3.txt')

array = re.findall(r"mul\(\d+,\d+\)", puzzle)

result = 0

for i in array:
    numbers = re.findall(r"\d+", i)
    result += int(numbers[0])*int(numbers[1])

print(result)