from d2_p1_parse import input_parse

valid = 0

for password in input_parse():
	valid += (int(password["min"]) <= password["password"].count(password["letter"]) <= int(password["max"]))

print(valid)