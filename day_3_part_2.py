import re
import openfile

puzzle = openfile.brutFile('day_3.txt')

array = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", puzzle)

result = 0
do_dont = True

for i in array:
    if i == 'do()':
        do_dont = True
    elif i == "don\'t()":
        do_dont = False
    elif do_dont:
        numbers = re.findall(r"\d+", i)
        result += int(numbers[0])*int(numbers[1])

print(result)