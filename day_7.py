from utils.openfile import readFile
import re
from itertools import product

puzzle = readFile("day_7.txt")

# Function de récupartion de la target ainsi que les nombre associer a celle-ci
def get_utils(line):
    target, numbers = line.split(":")
    convert_target = int(target)
    list_of_numbers = re.findall(r"\d+", numbers)
    return convert_target, list_of_numbers

# Function qui permet de ne pas resecter la logique mathématique. Opération effectuer de la gauche vers la droite.
def left_to_right(numbers, operateurs):
    result = int(numbers[0])
    for i, operateur in enumerate(operateurs):
        if operateur == '+':
            result+= int(numbers[i+1])
        elif operateur == '*':
            result *= int(numbers[i+1])
    return result

# Function qui avec itertools me permet de generer le nombre d'opération possible.
def test_line(target, numbers):
    #nouveau pour moi cette outils "product" permet de creer une liste de toute les opération possible
    #depuis une liste données dans mon cas pour chaque ligne on prend len moin un pour chaque espace 
    #disponible pour effectuer une opération.
    #puis pour chaque list d'opération je vais utiliser la function left to right pour ne pas subir 
    #la logique mathématique habituel.
    operations= list(product(['*', '+'], repeat=len(numbers)-1))
    for operation in operations:
        result = left_to_right(numbers, operation)
        if result == target:
            return True
    return False

result = 0         
for i in puzzle:
    target, numbers = get_utils(i)
    if test_line(target, numbers):
        result += target

print(result)