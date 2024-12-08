import re
import openfile

puzzle = openfile.readFile("day_4.txt")

# Création d'une fonction qui trouve chaque occurence de 'X' dans le puzzle.
def find_All_X(array):
    result = []
    for i in array:
        tampon = []
        for c, char in enumerate(i):
            if char == 'X':
                tampon.append(c)
        result.append(tampon)
    return result

# Function qui permet de trouver les occurence de 'XMAS' a partir des 'X' trouver dans le puzzle.
def find_XMAS(array, input_puzzle):

    direction = [
        (0, 1), (0, -1),    #droite, gauche
        (-1, 0), (1, 0),    #haut, bas
        (-1, 1), (-1, -1),  #diag haut droite, gauche
        (1, 1), (1, -1),    #diag bas droite, gauche
    ]

    count = 0
    string = "XMAS"
    string_length = len(string)

    rows = len(input_puzzle)
    cols = len(input_puzzle[0])

    for row_index, x_positions in enumerate(array):  
        for col_index in x_positions:  
            for dx, dy in direction:  
                found = True
                for k in range(1, string_length):  
                    new_row = row_index + k * dx
                    new_col = col_index + k * dy
                    if not (0 <= new_row < rows and 0 <= new_col < cols) or input_puzzle[new_row][new_col] != string[k]:
                        found = False
                        break
                if found:
                    count += 1
    return count

print(find_XMAS(find_All_X(puzzle), puzzle))
