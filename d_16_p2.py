from d_16_parse import input_parse
from functions import binary_insert
from math import prod

field_ranges, your_ticket, nearby_tickets = input_parse()

####	Filter out invalid tickets  (tried to do these two first blocks together but that was very messy)
valid_tickets = []
for ticket in nearby_tickets:
	valid_ticket = True
	for value in ticket:
		valid_value = False
		for ranges in field_ranges.values():
			for r in ranges:
				if r[0] <= value <= r[1]:
					valid_value = True
					break
		if not valid_value:
			valid_ticket = False
			break
	if valid_ticket:
		valid_tickets.append(ticket)

####	Narrow down possible fields for each position in the tickets
possible_fields = []
for i in range(len(valid_tickets[0])):
	possible_fields.append([])
	for field in field_ranges:
		field_pos_valid = True
		for ticket in valid_tickets:
			field_pos_valid_for_ticket = False
			for r in field_ranges[field]:
				if r[0] <= ticket[i] <= r[1]:
					field_pos_valid_for_ticket = True
					break
			if not field_pos_valid_for_ticket:
				field_pos_valid = False
				break
		if field_pos_valid:
			possible_fields[-1].append(field)

####	Create a list with the positions with the fewest possibilities at the start to make the next bit faster
amount_possible = []
for i in range(len(possible_fields)):
	binary_insert([i, possible_fields[i]], amount_possible, compare=lambda x: len(x[1]))

def iterate_valid_fields(amount_possible, already_taken={}):
	"""
	Function to recursively test all possible combinations of fields to find the valid one
	Unfortunately very specific to this problem and loads of assumptions have been made to make it faster
	Also has to "invert" the dict when returning final value as we want it to return a pos -> field map, but it is given a field -> pos map for convenience
	"""
	if len(amount_possible) == 0:
		return {already_taken[field]: field for field in already_taken}
	for field in amount_possible[0][1]:
		if not field in already_taken:
			return iterate_valid_fields(amount_possible[1:], dict(already_taken , **{field: amount_possible[0][0]}))

####	Finally takes the product of relevant entries in your_ticket
field_labels = iterate_valid_fields(amount_possible)
print(prod([your_ticket[i] for i in range(20) if field_labels[i].startswith("departure")]))