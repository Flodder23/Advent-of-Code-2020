from d5_parse import input_parse

seats = input_parse()
m = 0

for seat in seats:
	r = 0
	for i in range(7):
		if seat["row"][-(1+i)] == "B":
			r += 2 ** i
	c = 0
	for i in range(3):
		if seat["col"][-(1+i)] == "R":
			c += 2 ** i
	n = r * 8 + c
#	print(seat, r, c, n)
	if n > m:
		m = n

print(m)