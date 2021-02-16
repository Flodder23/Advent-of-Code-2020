from d_21_parse import input_parse
from functions import quicksort

info = input_parse()
allergen_ingredients = {}

for [ingredients, allergens] in info:
	for allergen in allergens:
		if allergen in allergen_ingredients:
			allergen_ingredients[allergen] = [ingredient for ingredient in allergen_ingredients[allergen] if ingredient in ingredients]
		else:
			allergen_ingredients[allergen] = ingredients

canonical_allergen_ingredients = {}
while len(allergen_ingredients) > len(canonical_allergen_ingredients):
	for allergen in allergen_ingredients:
		if len(allergen_ingredients[allergen]) == 1:
			ingredient = allergen_ingredients[allergen][0]
			canonical_allergen_ingredients[allergen] = ingredient
			for a in allergen_ingredients:
				if ingredient in allergen_ingredients[a]:
					allergen_ingredients[a].remove(ingredient)

print(",".join([canonical_allergen_ingredients[allergen] for allergen in sorted(allergen_ingredients)]))