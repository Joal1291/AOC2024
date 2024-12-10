import re
import openfile
from collections import Counter


puzzle = openfile.readFile("day_4.txt")

# Fonction qui trouve chaque occurence de 'M' dans le puzzle.
def find_All_M(array):
    result = []
    for i in array:
        tampon = []
        for c, char in enumerate(i):
            if char == 'M':
                tampon.append(c)
        result.append(tampon)
    return result

# Function qui permet de trouver les occurence de 'MAS' a partir des 'M' trouver dans le puzzle.
def find_MAS(array, input_puzzle):

    direction = [
        (-1, 1), (-1, -1),  #diag haut droite, gauche
        (1, 1), (1, -1),    #diag bas droite, gauche
    ]

    position_A = []

    string = "MAS"
    string_length = len(string)

    rows = len(input_puzzle)
    cols = len(input_puzzle[0])

    for row_index, m_positions in enumerate(array):  
        for col_index in m_positions:  
            for dx, dy in direction:
                found = True
                for k in range(1, string_length):
                    new_row = row_index + k * dx
                    new_col = col_index + k * dy
                    if not (0 <= new_row < rows and 0 <= new_col < cols) or input_puzzle[new_row][new_col] != string[k]:
                        found = False
                        break
                if found:
                    # Une fois une occurence de 'MAS' trouver j'enregistre la position du 'A'
                    # Ainsi si deux occurences de 'MAS' partage le même 'A' cela veut dire qu'une croix est former

                    a_row = row_index + dx
                    a_col = col_index + dy
                    position_A.append((a_row, a_col))

                    a_counts = Counter(position_A)

                    X_mas_count = sum(1 for pos, count in a_counts.items() if count > 1)

    return X_mas_count
    

print(find_MAS(find_All_M(puzzle), puzzle))

# Processus assé long plus de une seconde de recherche.