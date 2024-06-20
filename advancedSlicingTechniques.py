#Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 103, 104, 105, 106]

x = slice(7, 14)
second_week = temperatures[x]
print(second_week)

#Task 2

high_temp = []
for temperature in temperatures:
	if temperature > 100:
		high_temp.append(temperature)
print(high_temp)