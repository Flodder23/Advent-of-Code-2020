from d_19_parse import input_parse
import re

def to_regex(rules, n):
	if re.match(r"[a-z]", rules[n][0][0]):
		return rules[n][0][0]
	else:
		return "(" + "|".join([
			"(" +
			"".join([to_regex(rules, m) for m in rule])
			+ ")"
		for rule in rules[n]]) + ")"

if __name__ == "__main__":
	rules, messages = input_parse()
	regex = re.compile(to_regex(rules, "0"))
	print(sum([bool(regex.fullmatch(m)) for m in messages]))