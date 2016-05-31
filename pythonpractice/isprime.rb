

getprime = input("Enter a number: ")

def divisors(divisor):
	divides = false

	for i in range(1,divisor):
		if divisor % i == 0:
			divides = true

	return(divides)


def isprime(num):

	if divisors(num) = true
		print("Not a prime number")
	else
		print("Prime number")

isprime(getprime)