
array = [1, 2, 3, 4, 5, 2, 9, 7]
topline = input("Enter an upper bound: ")
newarray = []

def listbound(topline, array):

	for elem in array:
		if elem <= topline:
			newarray.append(elem)

	print(newarray)

listbound(topline,array)