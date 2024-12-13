import re
import openfile

puzzle = openfile.readFile('day_6.txt')

# je vais d'abbord commencer par ecrire ce qu'il faut pour trouver la position du garde.

def find_the_guard(array):
    for line in array:
        if re.findall(r"\^", line):
            direction = array[array.index(line)][line.index("^")]
            return array.index(line), line.index("^"), direction



def lets_move_and_count(position_y, position_x, direction, array):

    actual_y, actual_x = position_y, position_x
    position = True
    actual_direction = direction
    
    directions = { #direction qui me permettrons d'avancer dans l'espace que je n'ai pas utiliser lors de la premiere version   
        #car je n'ai pas su l'utiliser de même pour les turn!
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    turn = {
        "^":">",
        "v":"<",
        ">":"v",
        "<":"^"
    }
    visited_cases = []
    visited_cases.append((actual_y, actual_x))
    #j'ai donc coder ca a la dure et maintenant avec l'aide de chat je vais essayer de le réduire!!
    while position:
        if actual_direction == "^":
            if array[actual_y - 1][actual_x] != "#":
                actual_y-=1
            else:
                actual_x+=1
                actual_direction = ">"
        elif actual_direction == "v":
            if array[actual_y + 1][actual_x] != '#':
                actual_y+=1
            else:
                actual_x-=1
                actual_direction = "<"
        elif actual_direction == "<":
            if array[actual_y][actual_x-1] != '#':
                actual_x-=1
            else:
                actual_direction = "^"
                actual_y-=1
        elif actual_direction == ">":
            if array[actual_y][actual_x+1] != '#':
                actual_x+=1
            else:
                actual_y+=1
                actual_direction = 'v'
        if actual_x < 0 or actual_x >= len(array[0]) or actual_y < 0 or actual_y >= len(array) :
            position = False
        else:
            if (actual_y, actual_x) not in visited_cases:
                visited_cases.append((actual_y, actual_x))
        
    return len(visited_cases)

    # visited_cases = set()
    # actual_y, actual_x = position_y, position_x
    # visited_cases.add((actual_y, actual_x))  

    # while True:
    #     next_y = actual_y + directions[actual_direction][1]
    #     next_x = actual_x + directions[actual_direction][0]

    #     if next_x < 0 or next_x >= len(array[0]) or next_y < 0 or next_y >= len(array):
    #         break  

    #     if array[next_y][next_x] != '#':
    #         actual_y = next_y
    #         actual_x = next_x
    #         visited_cases.add((actual_y, actual_x))
    #     else:
    #         actual_direction = turn[actual_direction]

    # return len(visited_cases)



position_y, position_x, direction= find_the_guard(puzzle)

print(lets_move_and_count(position_y, position_x, direction, puzzle))

#version chat visiblement plus rapide de 200 centieme. 