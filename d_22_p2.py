### Optimised using ideas from here: 
### 	https://github.com/hltk/adventofcode/blob/main/2020/22.py,
### 	https://github.com/viliampucik/adventofcode/blob/master/2020/22.py

from d_22_parse import input_parse
from collections import deque
import itertools

def play(player1, player2, return_deck=False):
	history = set()
	while True:
		if (state := (tuple(player1), tuple(player2))) in history:
			return player1 if return_deck else 1
		history.add(state)
		p1 = player1.popleft()
		p2 = player2.popleft()
		if p1 > len(player1) or p2 > len(player2):
			winner = 1 if p1 > p2 else 2
		else:
			winner = play(
				deque(itertools.islice(player1, 0, p1)),
				deque(itertools.islice(player2, 0, p2))
			)
		if winner == 1:
			player1.extend((p1, p2))
		else:
			player2.extend((p2, p1))
		if len(player1) == 0:
			return player2 if return_deck else 2
		elif len(player2) == 0:
			return player1 if return_deck else 1


player1, player2 = input_parse()
winner = play(player1, player2, return_deck=True)
print(sum([(i+1) * winner.pop() for i in range(len(winner))]))