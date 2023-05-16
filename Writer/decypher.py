import sympy

array = input("Enter numeric values ​​as written separated by spaces or commas (don't remove numbers with commas from numbers):").split()

array = [num if isinstance(num, int) else int(num) if num.is_integer() else float(f'{num:.2f}') for num in array]
		

for i in range(len(array)):
    if sympy.isprime(array[i]):
    	array[i] = int(array[i])
    else:
    	array[i] = array[i]*2
    	array[i] = int(array[i])
    	
def decrypt(array):
	for char in array:
		print(chr(char),end='')

decrypt(array)
