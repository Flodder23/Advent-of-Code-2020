from d_17_parse import input_parse

def get_next_state(coords, active_cells, next_check):
	x, y, z, w = list(map(int, coords.split(",")))
	active_neighbours = 0
	for dx in (-1, 0, 1):
		for dy in (-1, 0, 1):
			for dz in (-1, 0, 1):
				for dw in (-1, 0, 1):
					if dx == 0 and dy == 0 and dz == 0 and dw == 0:
						continue
					cell_ref = f"{x+dx},{y+dy},{z+dz},{w+dw}"
					if cell_ref in active_cells:
						active_neighbours += 1
					else:
						if cell_ref in next_check:
							next_check[cell_ref] += 1
						else:
							next_check[cell_ref] = 1
	return active_neighbours in (2, 3)

active_cells = list(map(lambda c: c + ",0", input_parse()))
for _ in range(6):
	next_active = []
	next_check = {}
	for coords in active_cells:
		if get_next_state(coords, active_cells, next_check):
			next_active.append(coords)
	active_cells = next_active

	for coords in next_check:
		if next_check[coords] == 3:
			active_cells.append(coords)

print(len(active_cells))