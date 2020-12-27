from d_04_parse import input_parse

passports = input_parse()
valid = 0

for p in passports:
	valid += all([not (p[field] is None) for field in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")])

print(valid)