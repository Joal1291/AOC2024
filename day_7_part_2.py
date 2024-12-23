from openfile import readFile
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
        elif operateur == '||': # ligne ajouter pour la logique de calcul...
            result = int(str(result)+str(numbers[i+1]))
    return result

def test_line(target, numbers):
    operations= list(product(['*', '+',  '||'], repeat=len(numbers)-1)) # pour le day 2 j'ai finalement juste ajouter l'opérateur '||' concat et une ligne dans left to right
    for operation in operations:
        result = left_to_right(numbers, operation)
        if result == target:
            return True
    return False

result = 0         
for i in test:
    target, numbers = get_utils(i)
    if test_line(target, numbers):
        result += target 

print(result)

# Ok j'ai passe le test cependant le processus à pris 21 secondes ce qui est beaucoup trop 
# je pense que cela est du au fait qu'il test des ligne inutile 
# il faudrais pouvoir créer des ligne qui ne contienne pas deux ou trois fois l'opérateur concat
# car avec cette solution les ligne peuvent contenir plus de deux fois l'opéarateur concat alors 
# que je dois tester qu'une seule fois l'opérateur par ligne exemple pour une ligne tel que 
# 15 12 16 
# il doit tester 15 (* et +) 12 || 16
# puis 15 || 12 (* et +) 16
# est la solution actuel propose aussi cette ligne 15 || 12 || 16
# ce qui n'est pas demander du tout
