from d_20_parse import input_parse
from math import prod
import re

def get_sides(tile):
	return [
		[row[-1] for row in tile],
		tile[-1],
		[row[0] for row in tile],
		tile[0]
	]

def crop(tile):
	return [row[1:-1] for row in tile[1:-1]]

def rotate(tile, rot, flip):
#	print("TILE:")
#	for line in tile:
#		print("".join(line))
#	print()
	for _ in range(rot):
		tile = [[tile[-1-i][j] for i in range(len(tile))] for j in range(len(tile[0]))]
	return tile[::-1] if flip else tile

def get_side_matched(matches, id0, id1):
	for s in matches[id0]:
		if matches[id0][s]["id"] == id1:
			return s

def same_side(s0, s1):
	return all([s0[p] == s1[p] for p in range(len(s0))])

def common_side(t0, t1):
	s0s, s1s = get_sides(t0), get_sides(t1)
	for i in range(4):
		for j in range(4):
			for f in (True, False):
				if same_side(s0s[i], s1s[j][::-1] if f else s1s[j]):
					return i, j, f
	return None, None, None

def align(t0, t1, s1):
	"""Return rotation & flip needed so tile t0 matches tile t1 at given side s1"""
	s0 = (s1 + 2) % 4
	side_match = get_sides(t1)[s1]
	for rot in range(4):
		for flip in (False, True):
			if side_match == get_sides(rotate(t0, rot, flip))[s0]:
				return rot, flip


tiles = input_parse()#"d_20_input_example.txt")
ids = list(tiles.keys())
matches = {i: {} for i in ids}

# For each tile work out which tiles match which sides
for i in range(len(ids) - 1):
	id0 = ids[i]
	for j in range(i + 1, len(ids)):
		id1 = ids[j]
		s0, s1, flip = common_side(tiles[id0], tiles[id1])
		if not s0 is None:
			matches[id0][s0] = {
				"id": id1,
				"side": s1
			}
			matches[id1][s1] = {
				"id": id0,
				"side": s0
			}

# Get first corner piece
for prev_id in ids:
	if len(matches[prev_id]) == 2:
		break
for side in range(4):
	if side in matches[prev_id] and (side+1)%4 in matches[prev_id]:
		next_id = matches[prev_id][side]["id"]
		matches[prev_id][side-1] = {
			"id": 0#,
#			"side": 0,
		}  # Setting up for easier rotation things later
		break

image = [[0], [prev_id]]
tiles[prev_id] = rotate(tiles[prev_id], (-side) % 4, False)

# Create grid of tile IDs
while True:
	while True:
		image[-1].append(next_id)
		left_side = get_side_matched(matches, next_id, prev_id)
		right_side = (left_side + 2) % 4
		if not right_side in matches[next_id]:
			break
		prev_id = next_id
		next_id = matches[prev_id][right_side]["id"]
	above_id = image[-1][0]
	down_side = (get_side_matched(matches, above_id, image[-2][0]) + 2) % 4
	if not down_side in matches[above_id]:
		break
	prev_id = matches[above_id][down_side]["id"]
	image.append([prev_id])
	maybe_right_side = (get_side_matched(matches, prev_id, above_id) + 1) % 4
	if maybe_right_side in matches[prev_id]:
		right_side = maybe_right_side
	else:
		right_side = (maybe_right_side + 2) % 4
	next_id = matches[prev_id][right_side]["id"]
del image[0]

# Use grid of tile IDs to rotate & flip tiles to match
# (separate to above section because it got too long and complicated and buggy)
for y in range(len(image)):
	if y != 0:
		tiles[image[y][0]] = rotate(tiles[image[y][0]], *align(tiles[image[y][0]], tiles[image[y-1][0]], 1))
	for x in range(1, len(image[y])):
		tiles[image[y][x]] = rotate(tiles[image[y][x]], *align(tiles[image[y][x]], tiles[image[y][x-1]], 0))

for tile_row in image:
	for i in tile_row:
		tiles[i] = crop(tiles[i])

# Make "whole image" to search for monsters in, joining tiles up in grid
whole_image = [[]]
for tile_row in image:
	for i in range(8):
		for tile_id in tile_row:
			whole_image[-1].extend(tiles[tile_id][i])
		whole_image.append([])
del whole_image[-1]

monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """[1:]  # Remove first newline
for rot in range(4):
	for flip in (False, True):
		new_image = ["".join(row) for row in rotate(whole_image, rot, flip)]
		k = len(new_image[0])
		monsters = len(re.findall(r"(?=(#..{"+str(k-19)+"}#.{4}##.{4}##.{4}###.{"+str(k-19)+"}.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}))", "\n".join(new_image), re.DOTALL))
		if monsters > 0:
			print("".join(new_image).count('#') - (monsters * 15))
			break
