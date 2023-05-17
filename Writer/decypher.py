import sympy 

array = [56.0, 57.0, 55.5, 59.0, 48.5]

array = [num if isinstance(num, int) else int(num) if num.is_integer() else float(f'{num:.2f}') for num in array] 
                  
for i in range(len(array)): 
	array[i] = array[i]*2 
	array[i] = int(array[i]) 

def decrypt(array): 
	for char in array: 
		print(chr(char),end='') 

decrypt(array)