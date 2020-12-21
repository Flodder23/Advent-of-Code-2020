from d4_parse import input_parse

passports = input_parse("d4_input_example.txt")
valid = 0

for p in passports:
	valid += all([not (p[field] is None) for field in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")])

print(valid)