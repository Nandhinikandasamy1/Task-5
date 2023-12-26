in_number = 20
print(in_number)
for num in range(in_number + 1):
	out_str = ""
	for num1 in range(num):
		out_str = out_str + " " + str(num)
	print(out_str.center((3 * in_number) - 1))
