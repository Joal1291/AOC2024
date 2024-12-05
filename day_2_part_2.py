import re
import openfile

puzzle = openfile.readFile("day_2.txt")

result = 0

def check_new_line(new_numbers):

    for index, _ in enumerate(new_numbers):
        new_list = new_numbers[:index] + new_numbers[index + 1:]
        if check_line(new_list, True): return True


def check_line(numbers, removed=False):
    croissant = numbers[1] > numbers[0]
    decroissant = numbers[1] < numbers[0]

    for i in range(1, len(numbers)):
        actual = numbers[i]
        compare = numbers[i-1]

        if(
            (croissant and (actual < compare or actual - compare > 3)) or
            (decroissant and (actual > compare or compare - actual > 3)) or
            (actual == compare)
        ):
            if not removed:
                return check_new_line(numbers)
            else :
                return False
            
    return True


for line in puzzle:
    numbers = list(map(int, line.split()))
    if check_line(numbers):result +=1
    else: continue

print(result)