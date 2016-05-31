import random

def guessinggame():

	num = random.randint(1,9)
	guesscount = 1

	while True:

		guessinput = raw_input("Enter a number to guess: ")

		if guessinput == "exit":
			break
		
		guess = int(guessinput)

		if guess > num:
			print("Too high")
			guesscount += 1
		elif guess < num:
			print("Too low")
			guesscount += 1
		else:
			print("You got it!")
			print("You guessed " + str(guesscount) + " times.")
			guesscount = 1
			num = random.randint(1,9)



guessinggame()
