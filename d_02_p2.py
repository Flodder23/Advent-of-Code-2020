from d_02_p2_parse import input_parse

valid = 0

for password in input_parse():
	a, b, letter, password = [password[key] for key in ("a", "b", "letter", "password")]
	a, b = int(a) - 1, int(b) - 1
	valid += (((password[a] == letter) + (password[b] == letter)) % 2)

print(valid)