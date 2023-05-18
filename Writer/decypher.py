import os

array = eval(input("Enter the array: "))
if os.name == "nt":
    os.system("cls")  # Per Windows
else:
    os.system("clear")

for i in range(len(array)):
    array[i] = array[i] * 2
    array[i] = int(array[i])


def decypher(array):
    for char in array:
        print(chr(char), end="")


decypher(array)
