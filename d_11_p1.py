from d_11_parse import input_parse

def get_next_state(coords, layout):
	y, x = coords
	if layout[y][x] == ".":
		return "."
	dy_range = (
		-1 if y > 0 else 0,
		2 if y < len(layout) - 1 else 1
	)
	dx_range = (
		-1 if x > 0 else 0,
		2 if x < len(layout[y]) - 1 else 1
	)
	adjacent_occupied = 0
	for dy in range(*dy_range):
		for dx in range(*dx_range):
			if not (dx == 0 and dy == 0):
				adjacent_occupied += (layout[y+dy][x+dx] == "#")
	if layout[y][x] == "L" and adjacent_occupied == 0:
		return "#"
	elif layout[y][x] == "#" and adjacent_occupied >= 4:
		return "L"
	else:
		return layout[y][x]

def check_equivalent_layout(layout1, layout2):
	for y in range(len(layout1)):
		for x in range(len(layout1[y])):
			if layout1[y][x] != layout2[y][x]:
				return False
	return True


if __name__ == "__main__":
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