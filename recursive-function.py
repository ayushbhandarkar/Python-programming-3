def fact(num):
	if num == 1:
		return 1
	else:
		return num*fact(num-1)


num = 5
mult = fact(num)
print("factorial of {num} : {mult}")
