from d_22_parse import input_parse

player1, player2 = input_parse()

winner = None
while winner is None:
	p1 = player1.popleft()
	p2 = player2.popleft()
	if p1 > p2:
		player1.extend((p1, p2))
	else:
		player2.extend((p2, p1))
	
	if len(player1) == 0:
		winner = player2
	elif len(player2) == 0:
		winner = player1

print(sum([(i+1) * winner.pop() for i in range(len(winner))]))