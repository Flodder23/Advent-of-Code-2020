from d_06_parse import input_parse

print(sum([sum([any([letter in person for person in group]) for letter in "abcdefghijklmnopqrstuvwxyz"]) for group in input_parse()]))