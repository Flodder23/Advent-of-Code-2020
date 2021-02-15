from d_21_parse import input_parse

info = input_parse()
allergen_ingredients = {}

for [ingredients, allergens] in info:
	for allergen in allergens:
		if allergen in allergen_ingredients:
			allergen_ingredients[allergen] = [ingredient for ingredient in allergen_ingredients[allergen] if ingredient in ingredients]
		else:
			allergen_ingredients[allergen] = ingredients

# The following works if we assume an ingredient contains an allergen iff it is in the list for at least one allergen;
# This holds for my input, so I presume the puzzle was made this way

total = 0
for [ingredients, _] in info:
	for ingredient in ingredients:
		total += not(any([ingredient in allergen_ingredients[allergen] for allergen in allergen_ingredients]))
print(total)