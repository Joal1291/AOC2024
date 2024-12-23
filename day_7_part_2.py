from utils.openfile import readFile
from itertools import product
import re

puzzle = readFile('day_7.txt')

# nouvel opérateur "||" quand une ligne est fausee réssayer en concatenant deux chiffre cote a cote 
# si l'une des combinaison permet de valider l'opération je peut donc ajouter le nombre target
# au résultat final.

test = [
    "190: 10 19",
    "3267: 81 40 27", 
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]

def get_utils(line):
    target, numbers = line.split(":")
    convert_target = int(target)
    list_of_numbers = re.findall(r"\d+", numbers)
    return convert_target, list_of_numbers

def left_to_right(numbers, operateurs):
    result = int(numbers[0])
    for i, operateur in enumerate(operateurs):
        if operateur == '+':
            result+= int(numbers[i+1])
        elif operateur == '*':
            result *= int(numbers[i+1])
    return result

def test_line(target, numbers):
    operations= list(product(['*', '+'], repeat=len(numbers)-1))
    count = 1
    for operation in operations:
        result = left_to_right(numbers, operation)
        print(f"operation n° {count} avec les operateur {operation}")
        print(result)
        print("----")
        if result == target:
            return True
        count =+1
    return False

# Pour la seconde partie du jour 7 je vais juste ajouter une function qui vas prendre les ligne
# qui n'ont pas passer le premier test puis je vais créer un tableau dans le quelle sera inserer 
# toutes les nouvelle ligne qui auront concatener les deux nombre cote a cote
# exception fait des tableau avec just deux nombre qui sera directement concatenenr et tester

def find_new_line(target, numbers):
    if len(numbers) == 2:
        if target == int(str(numbers[0])+str(numbers[1])):
            return True
    else:
        array_of_new_line = []
        count=0
        for i in range(0, len(numbers)-1):
            tampon = []
            for j in range(0, len(numbers)):
                if j == count:
                    tampon.append(str(numbers[i])+str(numbers[i+1]))
                elif j == count+1:
                    continue
                else:
                    tampon.append(numbers[j])
            array_of_new_line.append(tampon)
            count+=1
        print(array_of_new_line)
        count = 1
        for i in array_of_new_line:
            print(f"---------- {count} ------------")
            if test_line(target, i):
                return True
            count+= 1

    return False

result = 0         
# for i in test:
target, numbers = get_utils(test[4])
if test_line(target, numbers):
    result += target
elif find_new_line(target, numbers):
    result += target
    

print(result)