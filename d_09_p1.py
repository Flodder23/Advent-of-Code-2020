from d_09_parse import input_parse

def search_sums(summands, target):
	for x in range(len(summands)):
		for y in range(x+1, len(summands)):
			if summands[x] + summands[y] == target:
				return True
	return False

preamble_length = 25
series = input_parse()

for i in range(preamble_length + 1, len(series)):
	if not search_sums(series[i - preamble_length:i], series[i]):
		print(series[i])
		break