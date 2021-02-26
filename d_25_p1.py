from d_25_parse import input_parse

def next_value(value, subject_number=7, prime_remainder=20201227):
	return (value * subject_number) % prime_remainder

def transform(loop_size, subject_number=7, prime_remainder=20201227):
	value = 1
	for _ in range(loop_size):
		value = next_value(value, subject_number, prime_remainder)
	return value

def get_loop_size(desired_number, subject_number=7, prime_remainder=20201227):
	loop_size = 0
	value = 1
	while value != desired_number:
		loop_size += 1
		value = next_value(value, subject_number, prime_remainder)
	return loop_size

card_public, door_public = input_parse()

card_loop_size = get_loop_size(card_public)
door_loop_size = get_loop_size(door_public)

print(transform(door_loop_size, card_public))