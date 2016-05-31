import random


def randomoverlap():

	bound = input("Enter an upper bound: ")

	x = random.randint(1,bound)
	a = random.sample(range(x), random.randint(1,x))
	b = random.sample(range(x), random.randint(1,x))

	overlap = [i for i in a if i in b]
	print(a)
	print(b)
	print(overlap)

randomoverlap()