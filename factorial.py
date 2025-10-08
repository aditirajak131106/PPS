# Type Content here...
def factorial(n):
	if n < 0:
		print('Enter a positive number')
	else:
		fact = 1
		for i in range(1, n+1):
			fact *= i
		print('Factorial of given number is :', fact)
num = int(input('Enter a number : '))
factorial(num)
