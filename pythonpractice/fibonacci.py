
def fibonacci(num):

	sumarray = [1,1]

	for i in range(2,num):
		sumarray.append(sumarray[i-1]+sumarray[i-2])

	return(sumarray)

fibnum = input("Please enter a number: ")
print(fibonacci(fibnum))