print("Input the first string:")
in_string1 = str(input())
print("Input the second string:")
in_string2 = str(input())
long_substring = ""
char_start_pos = 0
char_to_check = ""
substring_max = ""
substring_max_list = []
for char_start in in_string1:
	char_end_pos = char_start_pos
	for char_end in in_string1[char_start_pos:]:
		char_to_check = in_string1[char_start_pos:char_end_pos + 1]
		if char_to_check in in_string2:
			if (len(char_to_check) == (len(substring_max))):
				substring_max = char_to_check
				substring_max_list.append(substring_max)
			if (len(char_to_check) > (len(substring_max))):
				substring_max = char_to_check
				substring_max_list = []
				substring_max_list.append(substring_max)
		char_end_pos = char_end_pos + 1
	char_start_pos = char_start_pos + 1
print(substring_max_list)
print(" ".join(substring_max_list)) test
