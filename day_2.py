import re
import openfile

puzzle = openfile.readFile("day_2.txt")

result = 0
    
def check_line(line):
    numbers = list(map(int, line.split()))

    croissant = numbers[1] > numbers[0]
    decroissant = numbers[1] < numbers[0]

    for i in range(1, len(numbers)):
        actual = numbers[i]
        compare = numbers[i-1]

        if croissant and (actual < compare or actual - compare > 3): return False
        if decroissant and (actual > compare or compare - actual > 3): return False
        if actual == compare: return False

    return True

for line in puzzle:
    if check_line(line):result +=1
    else: continue

print(result)