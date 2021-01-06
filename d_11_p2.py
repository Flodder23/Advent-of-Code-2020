from d_11_parse import input_parse
from d_11_p1 import check_equivalent_layout

def get_next_state(coords, layout):
	y, x = coords
	if layout[y][x] == ".": return "."
	occupied = 0
	for dy in (-1, 0, 1):
		for dx in (-1, 0, 1):
			occupied += can_see_occupied_seat(coords, (dy, dx), layout)
	if layout[y][x] == "L" and occupied == 0:
		return "#"
	elif layout[y][x] == "#" and occupied >= 5:
		return "L"
	else:
		return layout[y][x]


def can_see_occupied_seat(coords, direction, layout):
	if direction == (0, 0): return False
	y, x = coords
	dy, dx = direction

	i = 1
	while 0 <= y + i*dy < len(layout) and 0 <= x + i*dx < len(layout[y]):
		if layout[y + i*dy][x + i*dx] == "#":
			return True
		elif layout[y + i*dy][x + i*dx] == "L":
			return False
		i += 1
	return False

layout = input_parse()

while True:
	next_layout = list(map(lambda row: row.copy(), layout))
	for y in range(len(layout)):
		for x in range(len(layout[y])):
			next_layout[y][x] = get_next_state((y, x), layout)
	if check_equivalent_layout(layout, next_layout):
		break
	layout = next_layout

print(sum([sum([seat == "#" for seat in row]) for row in layout]))