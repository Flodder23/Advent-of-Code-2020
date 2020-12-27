from d_01_parse import input_parse

report = input_parse()

for i in range(len(report)):
	a = report[i]
	for j in range(i+1, len(report)):
		b = report[j]
		if a + b == 2020:
			print(a * b)
		if a + b > 2020:
			break