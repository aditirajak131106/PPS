a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
c = float(input('Enter the third number: '))
if (a > b and a > c):
	print(f'Largest number: {a}\n')
elif (b > c and b > a):
	print(f'Largest number: {b}\n')
elif (c > a and c > b):
	print(f'Largest number: {c}\n')
else:
	print(f'Largest number: {a}\n')
