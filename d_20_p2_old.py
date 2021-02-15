from d_20_parse import input_parse
from math import prod

def get_sides(tile):
	return [
		[row[-1] for row in tile],
		tile[-1],
		[row[0] for row in tile],
		tile[0]
	]

def crop(tile):
	return []

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


tiles = input_parse("d_20_input_example.txt")
ids = list(tiles.keys())
matches = {i: {} for i in ids}

for i in range(len(ids) - 1):
	id0 = ids[i]
	for j in range(i + 1, len(ids)):
		id1 = ids[j]
		s0, s1, flip = common_side(tiles[id0], tiles[id1])
		if not s0 is None:
			matches[id0][s0] = {
				"id": id1,
				"side": s1,
				"flip": flip
			}
			matches[id1][s1] = {
				"id": id0,
				"side": s0,
				"flip": flip
			}

#get first corner piece
for first_id in ids:
	if len(matches[first_id]) == 2:
		break
for right_side in range(4):
	if right_side in matches[first_id] and (right_side+1)%4 in matches[first_id]:
		break

image_ids = [[first_id]]
image_tiles = tiles[first_id]

while True:
	while not image[-1][-1]["right"] is None:
		next_id = image[-1][-1]["right"]
		left_id = image[-1][-1]["id"]
		left_side = get_side_matched(matches, next_id, left_id)
		up_side = (left_side + 1) % 4
		right_side = (up_side + 1) % 4
		down_side = (right_side + 1) % 4
		up_id = matches[next_id][up_side]["id"] if up_side in matches[next_id] else None
		right_id = matches[next_id][right_side]["id"] if right_side in matches[next_id] else None
		down_id = matches[next_id][down_side]["id"] if down_side in matches[next_id] else None
		image[-1].append({
			"id": next_id,
			"right_side": right_side,
			"down_side": down_side,
			"left_side": left_side,
			"up_side": up_side,
			"right_id": right_id,
			"down_id": down_id,
			"left_id": left_id,
			"up_id": up_id
		})
	if image[-1][0]["down"] is None:
		break
	next_id = image[-1][0]["down"]
	up_side = get_side_matched(matches, next_id, image[-1][0]["id"])
	right_side = (up_side + 1 + (2 * int(matches[next_id][up_side]["flip"]))) % 4
	down_side = (right_side + 1 - (2 * int(matches[next_id][up_side]["flip"]))) % 4
	left_side = (down_side + 1 + (2 * int(matches[next_id][up_side]["flip"]))) % 4
	right_id = matches[next_id][right_side]["id"] if right_side in matches[next_id] else None
	down_id = matches[next_id][down_side]["id"] if down_side in matches[next_id] else None
	left_id = matches[next_id][left_side]["id"] if left_side in matches[next_id] else None
	image.append([{
		"id": next_id,
		"right_side": right_side,
		"down_side": down_side,
		"left_side": left_side,
		"up_side": up_side,
		"right_id": right_id,
		"down_id": down_id,
		"left_id": left_id,
		"up_id": image[-1][0]["id"]
	}])