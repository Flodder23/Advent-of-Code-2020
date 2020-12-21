from d5_parse import input_parse
from d5_p1 import get_seat_number
from functions import binary_insert

seat_numbers = []
for seat in input_parse():
	binary_insert(get_seat_number(seat), seat_numbers)

d = seat_numbers[0]
below = 0
above = len(seat_numbers) - 1
while above - below > 0:
	midpoint = (below + above) // 2
	if seat_numbers[midpoint] - midpoint == d + 1:
		above = midpoint - 1
	elif seat_numbers[midpoint] - midpoint == d:
		below = midpoint + 1
print(seat_numbers[below - 5:above + 5])