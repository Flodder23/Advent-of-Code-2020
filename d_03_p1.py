from d_03_parse import input_parse

map = input_parse()
trees = 0
x = 0

for y in range(1, len(map)):
	x += 3
	if x >= len(map[y]):
		x -= len(map[y])
	trees += (map[y][x] == "#")

print(trees)