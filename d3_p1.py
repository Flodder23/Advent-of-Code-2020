from d3_parse import input_parse

map = input_parse()
trees = 0
x = 0

for y in range(1, len(map)):
	x += 3
	if x >= len(map[y]):
		x -= len(map[y])
#	print(map[y][0:x] + "(" + map[y][x] + ")" + map[y][x+1:-1])
	trees += (map[y][x] == "#")

print(trees)