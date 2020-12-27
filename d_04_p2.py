from d_04_parse import input_parse
import re

passports = input_parse()
valid = 0

for p in passports:
	height_info = re.search(r"^(\d+)(\S+)$", p["hgt"]) if not p["hgt"] is None else None
	height, units = height_info.groups() if not (height_info is None) else ["", ""]
	valid += all([
		p["byr"] and len(p["byr"]) == 4 and (1920 <= int(p["byr"]) <= 2002),
		p["iyr"] and len(p["iyr"]) == 4 and (2010 <= int(p["iyr"]) <= 2020),
		p["eyr"] and len(p["eyr"]) == 4 and (2020 <= int(p["eyr"]) <= 2030),
		(units == "cm" and (150 <= int(height) <= 193)) or (units == "in" and (59 <= int(height) <= 76)),
		p["hcl"] and re.match(r"^#([0-9]|[a-f]){6}$", p["hcl"]),
		p["ecl"] and p["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
		p["pid"] and re.match(r"^[0-9]{9}$", p["pid"])
	])

print(valid)