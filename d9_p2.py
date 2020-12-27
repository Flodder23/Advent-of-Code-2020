from d9_parse import input_parse

target = 57195069
series = input_parse()

for i in range(len(series)):
	j = i + 1
	while sum(series[i:j]) < target:
		j += 1
	if sum(series[i:j]) == target:
		print(min(series[i:j]) + max(series[i:j]))
		break