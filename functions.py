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

def change_base(n, a, b, force_len=None):
	"""
	Given a base-a number n convert it to base b.
	returns a string so as not to confuse with int types etc.
	if force_len is given an integer value, the returned value is made to be of a suitable length by adding leading zeros.
	(the returned value is not changed if it has length >= force_len)
	"""
	n = str(n)
	n = sum([int(n[i]) * a**(len(n) - 1 - i) for i in range(len(n))])
	
	i = 0
	while b**i < n:
		i += 1
	i -= 1
	t = ""
	while i >= 0:
		j = 0
		while b**i <= n:
			n -= b**i
			j += 1
		t += str(j)
		i -= 1
	if force_len is not None and len(t) < force_len:
		t = "0"*(force_len - len(t)) + t
	return t
