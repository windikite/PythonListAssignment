#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

#Task 2
sum = 0
for grade in grades:
	sum += grade
average = sum / len(grades)
print(average)
