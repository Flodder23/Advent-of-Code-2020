import re

def input_parse(filename="d_04_input.txt"):
	raw = open(filename, "r").read().split("\n\n")
	passports = []
	for p in raw:
		passport = {}
		for field in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"):
			match = re.search(r"(\s|^)%s:(?P<%s>\S+)(\s|$)"%(field, field), p)
			if match:
				passport[field] = match.groupdict()[field]
			else:
				passport[field] = None
		passports.append(passport)
	return passports

if __name__ == "__main__":
	print(input_parse())