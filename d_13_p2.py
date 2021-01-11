from d_13_parse import input_parse

ids = input_parse()[1]

time = ids[0]
period = ids[0]
for i in range(1, len(ids)):
	if ids[i] == "x":
		continue
	while (time + i) % ids[i] != 0:
		time += period
	period *= ids[i]	# this should be period = lcm(period, id) but all inputs are prime so lcm(period, id) = period * id
print(time)