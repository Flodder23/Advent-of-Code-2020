import re

def input_parse(filename="d_21_input.txt"):
	raw = open(filename, "r").read().split("\n")
	info = []
	for food in raw:
		food_match = re.fullmatch(r"(?P<ingredients>(\w| )+) \(contains (?P<allergens>(\w|, )+)\)", food).groupdict()
		info.append([food_match["ingredients"].split(" "), food_match["allergens"].split(", ")])
	return info

if __name__ == "__main__":
	print(input_parse())