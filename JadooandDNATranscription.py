value = input()
len_value = len(value)
list1 = []
for i in range(0, len_value, 1):
	if value[i] == "G":
		list1.append("C")
	elif value[i] == "C":
		list1.append("G")
	elif value[i] == "T":
		list1.append("A")
	elif value[i] == "A":
		list1.append("U")
	else:
		print("Invalid Input")
		exit(0)
print(*list1, sep="")
