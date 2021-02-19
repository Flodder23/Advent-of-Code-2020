from d_23_parse import input_parse

def remove_cups(cups, pos, no=3):
	return [cups.pop(pos % len(cups)) for _ in range(no)]

def get_next_cup(pos):
	return (pos - 2) % 9 + 1
	

cups = input_parse()

for _ in range(100):
	current_cup = cups[0]
	cups_removed = remove_cups(cups, 1)
	destination_cup = get_next_cup(current_cup)
	while destination_cup in cups_removed:
		destination_cup = get_next_cup(destination_cup)
	destination_pos = cups.index(destination_cup) + 1
	cups = cups[:destination_pos] + cups_removed + cups[destination_pos:]
	cups.append(cups.pop(0))

one_pos = cups.index(1)
print("".join(map(str, cups[one_pos + 1:] + cups[:one_pos])))