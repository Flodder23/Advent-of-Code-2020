from functions import binary_insert

def input_parse(filename="d_17_input.txt"):
	raw = open(filename, "r").read().split("\n")
	active_cells = []
	for x in range(len(raw)):
		for y in range(len(raw[x])):
			if raw[x][y] == "#":
				active_cells.append(f"{x},{y},0")
	return active_cells

if __name__ == "__main__":
	print(input_parse())