from d_16_parse import input_parse

field_ranges, your_ticket, nearby_tickets = input_parse()

error_rate = 0
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
			error_rate += value
			break
print(error_rate)