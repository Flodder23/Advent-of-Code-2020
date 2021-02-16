from collections import deque

def input_parse(filename="d_22_input.txt"):
	raw = open(filename, "r").read().split("\n")
	player1 = deque()
	i = 1
	while raw[i] != "":
		player1.append(int(raw[i]))
		i += 1
	i += 2
	player2 = deque()
	while i < len(raw):
		player2.append(int(raw[i]))
		i += 1
	return player1, player2

if __name__ == "__main__":
	print(input_parse())