from d_23_parse import input_parse

def get_next_cup(pos):
	return (pos - 2) % 1_000_000 + 1

cups = input_parse()
successor = [i+1 for i in range(1_000_001)]
for pos in range(len(cups) - 1):
	successor[cups[pos]] = cups[pos + 1]
successor[cups[-1]] = len(cups) + 1
successor[-1] = cups[0]

current_cup = cups[0]
for _ in range(10_000_000):
	removed_cups = [successor[current_cup]]
	for _ in range(2):
		removed_cups.append(successor[removed_cups[-1]])
	successor[current_cup] = successor[removed_cups[-1]]
	destination_cup = get_next_cup(current_cup)
	while destination_cup in removed_cups:
		destination_cup = get_next_cup(destination_cup)
	after = successor[destination_cup]
	successor[destination_cup] = removed_cups[0]
	successor[removed_cups[2]] = after
	current_cup = successor[current_cup]

print(successor[1] * successor[successor[1]])