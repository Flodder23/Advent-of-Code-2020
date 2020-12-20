from functions import quicksort

def input_parse():
	raw = open("d1_input.txt", "r").readlines()
	return quicksort(list(map(int, raw)))

if __name__ == "__main__":
	print(input_parse())