from d_19_parse import input_parse
from d_19_p1 import to_regex
import re

rules, messages = input_parse()
rules["8"] = [[42], [42, 8]]	##  (not necessary to change these but it felt right)
rules["11"] = [[42, 31], [42, 11, 31]]

r_42 = to_regex(rules, "42")
r_31 = to_regex(rules, "31")

##  Basically we end up with r_0 matching r_42 being matched n>=1 times followed
##  by r_42 being matched m>=1 times then r_31 being matched m times too.
##  So we can match strings that contain n 42s at the start and m 31s at the end
##  and check that n >= 2, m >= 1 and n > m. (This simplifies to 1 <= m < n)

total = 0
for message in messages:
	l = 0
	n = 0
	match = re.match(f"(?P<n>{r_42})", message[l:])
	while match:
		n += 1
		l += len(match.groupdict()["n"])
		match = re.match(f"(?P<n>{r_42})", message[l:])
	
	m=0
	match = re.match(f"(?P<m>{r_31})", message[l:])
	while match:
		m += 1
		l += len(match.groupdict()["m"])
		match = re.match(f"(?P<m>{r_31})", message[l:])
	
	if 1 <= m < n and l == len(message):
		total += 1
print(total)
