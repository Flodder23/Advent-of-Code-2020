from d10_parse import input_parse
from functions import quicksort

joltages = [0] + quicksort(input_parse())
joltages = list(map(lambda x: {"value": x, "arrangements": 0}, joltages))
joltages = joltages + [{"value": joltages[-1]["value"] + 3, "arrangements": 1}]

for i in range(len(joltages)-2, -1, -1):
	j = 1
	while i + j < len(joltages) and joltages[i+j]["value"] - joltages[i]["value"] <= 3:
		if joltages[i+j]["value"] - joltages[i]["value"] <= 3:
			if joltages[i]["arrangements"] == 0:
				joltages[i]["arrangements"] = joltages[i+j]["arrangements"]
			else:
				joltages[i]["arrangements"] += joltages[i+j]["arrangements"]
		j += 1

print(joltages[0]["arrangements"])