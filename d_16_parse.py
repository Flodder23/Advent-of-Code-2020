import re

def input_parse(filename="d_16_input.txt"):
	raw = open(filename, "r").read().split("\n")
	
	i= 0
	field_ranges = {}
	field_range_regex = r"(?P<field>(\w| )+): (?P<lo0>\d+)-(?P<up0>\d+) or (?P<lo1>\d+)-(?P<up1>\d+)"
	while raw[i] != "":
		field_range = re.fullmatch(field_range_regex, raw[i]).groupdict()
		field_ranges[field_range["field"]] = [[int(field_range[ul + n]) for ul in ("lo", "up")] for n in ("0", "1")]
		i += 1
	
	i += 2
	your_ticket = list(map(int, raw[i].split(",")))
	
	nearby_tickets = [list(map(int, raw[j].split(","))) for j in range(i+3, len(raw))]
	
	return field_ranges, your_ticket, nearby_tickets

if __name__ == "__main__":
	print(input_parse())
