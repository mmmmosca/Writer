import os
characters = []
def cypher(text):
    for char in text:
        char = ord(char)
        if char % 2 == 0:
            characters.append(char/2)
            print("[.+%(",end='')
        elif char % 3 == 0:
            characters.append(char/2)
            print("};,!]",end='')
        elif char % 5 == 0:
            characters.append(char/2)
            print("$+)?|",end='')
        elif char % 7 == 0:
            characters.append(char/2)
            print("^'<:§",end='')
        elif char % 9 == 0:
            characters.append(char/2)
            print("#-_°=",end='')
        else:
            characters.append(char/2)
    print("\n"+str(characters))

text = input()
if os.name == 'nt':
        os.system('cls')  # Per Windows
    else:
        os.system('clear')
cypher(text)