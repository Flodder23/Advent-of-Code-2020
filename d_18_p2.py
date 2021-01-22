from d_18_parse import input_parse
from d_18_p1 import evaluate

def parse_expression(expression):
	i = 0
	while i < len(expression):
		if type(expression[i]) is list:
			parse_expression(expression[i])
		elif expression[i] == "+" and len(expression) > 3:
			new_expr = expression[i-1:i+2]
			del expression[i-1:i+1]
			expression[i-1] = new_expr
			i -= 2
		i += 1

t = 0
for expression in input_parse():
	parse_expression(expression)
	t += evaluate(expression)
print(t)