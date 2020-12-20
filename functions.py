def quicksort(arr, compare=lambda x, y: x < y):
	pivot = arr.pop(0)
	above, below = [], []
	for a in arr:
		if compare(a, pivot):
			above.append(a)
		else:
			below.append(a)
	if len(above) > 1:
		above = quicksort(above)
	if len(below) > 1:
		below = quicksort(below)
	return above + [pivot] + below
