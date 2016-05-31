

getprime = input("Enter a number: ")

def divisors(divisor):
	divides = False

	for i in range(2,divisor):
		if divisor % i == 0:
			divides = True

	return(divides)


def isprime(num):

	prime = ""

	if divisors(num) == True:
		prime = "Not a prime number"
	else:
		prime = "Prime number"

	if num == 1 or num == 2:
		prime = "Not a prime number"

	print(prime)
	return(prime)

isprime(getprime)