from d_10_parse import input_parse
from functions import quicksort

joltages = [0] + quicksort(input_parse())

diffs = {1: 0, 3: 1}  # always difference of 3 from last adapter to device
for i in range(1, len(joltages)):
	diffs[joltages[i] - joltages[i-1]] += 1

print(diffs[1] * diffs[3])