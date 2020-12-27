from functions import quicksort

def input_parse(filename="d_01_input.txt"):
	raw = open(filename, "r").readlines()
	return quicksort(list(map(int, raw)))

if __name__ == "__main__":
	print(input_parse())