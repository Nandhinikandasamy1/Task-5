print("Input the string:")
in_string = str(input())
checked_char = []
max_count = 0
for char in in_string:
	if char not in checked_char:
		if in_string.count(char) >= max_count:
			max_count = in_string.count(char)
		checked_char.append(char)
for char_to_print in checked_char:
    if in_string.count(char_to_print) == max_count:
        print(char_to_print + " " + str(max_count))
