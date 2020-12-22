from d7_parse import input_parse

def amount_contained(colour, contain_dict):
	return sum([
		c["amount"] * (1 + amount_contained(c["colour"], contain_dict)) for c in contain_dict[colour]
	])

contain_dict = input_parse()

print(amount_contained("shiny gold", contain_dict))