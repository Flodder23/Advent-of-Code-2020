from d_22_parse import input_parse
from collections import deque
from time import time

def compare_deque(d1, d2):
	return len(d1) == len(d2) and all([d1[i] == d2[i] for i in range(len(d1))])

def play(player1, player2, history, game=1):
#	print(f"\n=== Game {game} ===")
	r = 0
	winner = None
	while winner is None:
		r += 1
#		print(f"\n-- Round {r} (Game {game}) --")
#		print(f"Player 1's deck: {', '.join([str(n) for n in player1])}")
#		print(f"Player 2's deck: {', '.join([str(n) for n in player2])}")
		if any([compare_deque(player1, d1) and compare_deque(player2, d2) for [d1, d2] in history]):
#			print("déjà vu")
			return player1, 1
		history.append([player1.copy(), player2.copy()])
		p1 = player1.popleft()
		p2 = player2.popleft()
#		print(f"Player 1 plays: {p1}")
#		print(f"Player 2 plays: {p2}")
		if p1 > len(player1) or p2 > len(player2):
			if p1 > p2:
				player1.extend((p1, p2))
#				print(f"Player 1 wins game {game}, round {r}!")
			else:
				player2.extend((p2, p1))
#				print(f"Player 2 wins game {game}, round {r}!")
		else:
#			print("Playing a sub-game to determine the winner...")
			p1c, p2c = player1.copy(), player2.copy()
			_, no = play(deque([p1c.popleft() for _ in range(p1)]), deque([p2c.popleft() for _ in range(p2)]), history.copy())
#			print(f"\n...anyway, back to game {game}.")
			if no == 1:
				player1.extend((p1, p2))
#				print(f"Player 1 wins game {game}, round {r}!")
			else:
				player2.extend((p2, p1))
#				print(f"Player 2 wins game {game}, round {r}!")
		if len(player1) == 0:
			winner = player2
			no = 2
		elif len(player2) == 0:
			winner = player1
			no = 1
	return winner, no


player1, player2 = input_parse()#"d_22_input_example.txt")

t1 = time()
winner, _ = play(player1, player2, [])
print(time() - t1)

print(sum([(i+1) * winner.pop() for i in range(len(winner))]))