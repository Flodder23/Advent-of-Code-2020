from d_05_parse import input_parse

def get_seat_number(seat):
	r = 0
	for i in range(7):
		if seat["row"][-(1+i)] == "B":
			r += 2 ** i
	c = 0
	for i in range(3):
		if seat["col"][-(1+i)] == "R":
			c += 2 ** i
	return r * 8 + c

if __name__ == "__main__":
	print(get_seat_number(max(input_parse(), key=get_seat_number)))