path = "C:/Users/jordy/Documents/Code/algorithmie/AOC2024/puzzle_input/"

def readFile(filename: str):
    fichier = open(path+filename, 'r')
    words = []
    for line in fichier:
        words.extend(line.strip().split('\n'))
    # print(words)
    return words