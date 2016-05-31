divisor = input("Input a number: ")
newarray = []

def divisors(divisor):
	for i in range(1,divisor):
		if divisor % i == 0:
			newarray.append(i)

	print(newarray)

divisors(divisor)