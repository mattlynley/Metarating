import random


def passgenerator(size):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	nums = '1234567890'
	symbols = '!@#$%^&*'
	password = ""

	for i in range(1,size):

		choice = random.randint(1,4)

		if choice == 1:
			picker = random.randint(1,26)
			password += str(letters[picker-1])
		elif choice == 2:
			picker = random.randint(1,26)
			password += str(capletters[picker-1])
		elif choice == 3:
			picker = random.randint(1,10)
			password += str(nums[picker-1])
		else:
			picker = random.randint(1,8)
			password += str(symbols[picker-1])

	return(password)

passsize = input("Please enter a password size: ")
print(passgenerator(passsize))