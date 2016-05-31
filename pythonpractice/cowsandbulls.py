import random

def cowsandbulls():

	num = str(random.randint(1,9999))
	cows = 0
	bulls = 0

	while True:
		nums = raw_input("Enter a number: ")
		cows = 0
		bulls = 0
		j = 0
		if nums == num:
			print("Right number")
			break

		for i in nums:
			print(i)
			if i in num:
				cows += 1
				print(cows)
			if i == num[j]:
				bulls += 1
				cows -= 1
				print("Match: " + str(j))
			j += 1
		print("Cows: " + str(cows))
		print("Bulls: " + str(bulls))

cowsandbulls()