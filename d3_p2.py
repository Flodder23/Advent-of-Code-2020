from d3_parse import input_parse

map = input_parse()
trees = 0
total_trees = 1

for [dx, dy] in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
	trees, x, y = 0, 0, 0
	while y < len(map):
		if x >= len(map[y]):
			x -= len(map[y])
		trees += (map[y][x] == "#")
#		print(map[y][0:x] + "(" + map[y][x] + ")" + map[y][x+1:-1])
		x += dx
		y += dy
	total_trees *= trees

print(total_trees)