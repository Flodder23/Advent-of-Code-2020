def quicksort(arr, compare=int):
	pivot = arr.pop(0)
	above, below = [], []
	for a in arr:
		if compare(a) < compare(pivot):
			above.append(a)
		else:
			below.append(a)
	if len(above) > 1:
		above = quicksort(above)
	if len(below) > 1:
		below = quicksort(below)
	return above + [pivot] + below

def binary_insert(item, arr, compare=int, below=None, above=None, item_value=None):
	if item_value is None:
		item_value = compare(item)
	if below is None:
		below = 0
	if above is None:
		above = len(arr) - 1

	if above - below == 0:
		if item_value < compare(arr[below]):
			return arr.insert(below, item)
		else:
			return arr.insert(below + 1, item)
	elif above - below < 0:
		return arr.insert(below, item)

	midpoint = (below + above) // 2
	midpoint_value = compare(arr[midpoint])

	if item_value < midpoint_value:
		return binary_insert(item, arr, compare, below, midpoint - 1, item_value)
	elif midpoint_value < item_value:
		return binary_insert(item, arr, compare, midpoint + 1, above, item_value)
	else:
		return arr.insert(midpoint, item)