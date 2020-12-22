from d7_parse import input_parse

def can_hold_gold(colour, contains, contained_in=[], confirmed={}):
	if confirmed[colour] is None:
		for c in contains[colour]:
			if c in contained_in:  # if there is a loop
				continue
			if c == "shiny gold" or can_hold_gold(c, contains, contained_in + [colour], confirmed):
				confirmed[colour] = True
				return True
		confirmed[colour] = False
		return False
	else:
		return confirmed[colour]

contain_dict = input_parse()
contains = {colour: [c["colour"] for c in contain_dict[colour]] for colour in contain_dict}
confirmed = {colour: None for colour in contains}

print(sum([
	can_hold_gold(colour, contains, confirmed=confirmed) for colour in contains
]))