import re 
import openfile

puzzle = openfile.readFile('day_5.txt')

def get_rules_and_sequence(entry):
    rules = []
    sequences = []
    for i in entry:
        if re.match(r"\d+\|\d+", i):
            rules.append(i)
        elif re.match(r"^(\d{2})(,\d{2})*$", i):
            sequences.append(i)
    
    return rules, sequences


def get_rules_for_the_sequence(array_of_rules, line_sequence):

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

# pour la partie deux de la journée je vais me servir de cette function juste pour checker si les sequence sont bonne
# ainsi si elle sont mauvaise j'utiliserais la fonction reaaranged_the_false_sequences() pour les ranger dans le bonne ordre 
# et renvoyer le résultat attendu
def check_if_the_sequence_is_good(array, numbers):
    # Fonction qui vérifie si un nombre dans une séquence ne respecte pas une règle par rapport aux nombres précédents.
    # Si une règle existe entre un nombre actuel et un nombre précédent, 
    # la fonction s'arrête et renvoie 0. Sinon, le nombre à additionner au résultat final.
    numbers_to_check =[]
    numbers_to_check.append(numbers[0])
    for n in range (1, len(numbers)):
        number = numbers[n]
        for i in numbers_to_check:
            pattern = f"{number}|{i}"
            if pattern in array:
                return False
        numbers_to_check.append(number)
    return True

def rearranged_the_false_sequences(array, numbers):

    new_numbers_line = numbers [:] # nouvelle ligne qui peut etre modifier
    numbers_to_checked = []
    numbers_to_checked.append(numbers[0])

    for n in range(1, len(numbers)):
        number = numbers[n]
        for checked_number in numbers_to_checked:
            pattern = f"{number}|{checked_number}"
            if pattern in array:
                #prise de la position indiquer par les regles
                new_pos = new_numbers_line.index(checked_number)
                new_numbers_line.remove(number)
                new_numbers_line.insert(new_pos, number)
                # j'utilise mon ancienne fonction pour savoir si la sequence est bonne ou non et si
                # tel est le cas elle renvoie le nombre a additionner
                if check_if_the_sequence_is_good(array, new_numbers_line):
                    return int(new_numbers_line[(int((len(new_numbers_line)-1)/2))])
                # dans le cas contraire on continue a réarranger la sequence
                else:
                    return rearranged_the_false_sequences(array, new_numbers_line)
        numbers_to_checked.append(number)



result = 0
rules, sequences = get_rules_and_sequence(puzzle)

for sequence in sequences:
    numbers = list(map(int, sequence.split(',')))
    array_of_rules_for_the_sequence = get_rules_for_the_sequence(rules, sequence)
    if not check_if_the_sequence_is_good(array_of_rules_for_the_sequence, numbers):
        result += rearranged_the_false_sequences(array_of_rules_for_the_sequence,numbers)

print(f"result = {result}")

# putain process beaucoup trop long plus de 2 sec moin de 3 sec