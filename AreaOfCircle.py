# write your code here
def findArea(r):
	if rad<0 or rad > 100:
		print('Enter a positive value upto 100')
		return None
	else:
		return 3.14 * r * r
rad = float(input('Enter the radius : '))
x = findArea(rad)
if x is not None:
	print('Area of circle =', format(x, '.6f'))
