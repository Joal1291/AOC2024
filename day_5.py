import re
import openfile 

puzzle = openfile.readFile('day_5.txt')

def get_rules_and_sequence(entry):
    #récupération des donnés
    #tableau des règles à suivre
    #tableau des séquences à analyser
    rules = []
    sequences = []
    for i in entry:
        if re.match(r"\d+\|\d+", i):
            rules.append(i)
        elif re.match(r"^(\d{2})(,\d{2})*$", i):
            sequences.append(i)
    
    return rules, sequences


def get_rules_for_the_sequence(array_of_rules, line_sequence):
    #récupérer les donné associer a la sequence donné
    #renvoi un tableau spécifique pour cette cette sequence
    numbers = list(map(int, line_sequence.split(",")))
    array_of_rules_for_the_all_sequence = []

    for i in numbers:
        regex_pattern = rf"(\d+)\|{i}|{i}\|(\d+)"
        for rule in array_of_rules:
            if re.search(regex_pattern, rule):
                num1, num2 = map(int, rule.split('|'))
                if num1 in numbers and num2 in numbers:
                    pattern = f"{num1}|{num2}"
                    if pattern not in array_of_rules_for_the_all_sequence:
                        array_of_rules_for_the_all_sequence.append(rule)
    
    return array_of_rules_for_the_all_sequence


def check_if_the_sequence_is_good(array, line_sequence):
    # Fonction qui vérifie si un nombre dans une séquence ne respecte pas une règle par rapport aux nombres précédents.
    # Si une règle existe entre un nombre actuel et un nombre précédent, 
    # la fonction s'arrête et renvoie 0. Sinon, le nombre à additionner au résultat final.

    numbers = list(map(int, line_sequence.split(",")))
    numbers_to_check =[]
    numbers_to_check.append(numbers[0])
    for n in range (1, len(numbers)):
        number = numbers[n]
        for i in numbers_to_check:
            pattern = f"{number}|{i}"
            if pattern in array:
                return 0
        numbers_to_check.append(number)

    return int(numbers[(int((len(numbers)-1)/2))])


result = 0
rules, sequences = get_rules_and_sequence(puzzle)

for sequence in sequences:
    array_of_rules_for_the_sequence = get_rules_for_the_sequence(rules, sequence)
    add = check_if_the_sequence_is_good(array_of_rules_for_the_sequence, sequence)
    result+=add

print(f"result = {result}")
    

# temps d'exécution trop long supérieur à 2 seconde