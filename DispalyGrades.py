subject1 = float(input('subject 1: '))
subject2 = float(input('subject 2: '))
subject3 = float(input('subject 3: '))
subject4 = float(input('subject 4: '))
subject5 = float(input('subject 5: '))
avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5
print(f"Average Marks: {avg:.2f}")
if(avg >= 90 and avg <= 100):
	print('Grade: A')
elif(avg >= 80 and avg <= 89):
	print('Grade: B')
elif(avg >=70 and avg <= 79):
	print('Grade: C')
elif(avg >= 60 and avg <= 69):
	print('Grade: D')
else:
	print('Grade: F')
