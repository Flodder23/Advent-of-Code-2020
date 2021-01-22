import re

def input_parse(filename="d_19_input.txt"):
	raw = open(filename, "r").read().split("\n")
	rules = {}
	i = 0
	while raw[i] != "":
		r = re.match(r"(?P<n>\d+): (?P<rule>.+)", raw[i]).groupdict()
		rules[r["n"]] = [
			[
				value.replace("\"", "")
				for value in rule.split(" ")
			]
			for rule in r["rule"].split(" | ")
		]

		i += 1
	
	return rules, raw[i+1:]

if __name__ == "__main__":
	print(input_parse())