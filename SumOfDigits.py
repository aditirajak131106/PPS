num = int(input("num: "))
sum_of_digits = 0
for digit in str(num):
	sum_of_digits += int(digit)
print("sum:", sum_of_digits)
