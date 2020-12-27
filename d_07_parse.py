import re

def input_parse(filename="d_07_input.txt"):
	raw = open(filename, "r").readlines()
	rules = {}
	for rule in raw:
		colour = re.search(r"(?P<colour>.+) bags contain ", rule).groupdict()["colour"]
		rules[colour] = []
		for contained in re.findall(r"(\d+) ((\w| )+) bags?(, |\.)", rule):
			rules[colour].append({
				"amount": int(contained[0]),
				"colour": contained[1]
			})
	return rules

if __name__ == "__main__":
	print(input_parse())