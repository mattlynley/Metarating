string = raw_input("Please input a word: ")

print(string[len(string):0])

def ispalindrome(string):
	newstring = ""
	length = len(string) - 1

	while length >= 0:
		newstring += string[length]
		length -= 1

	if newstring == string:
		print("Palindrome")
	else:
		print("Not a palindrome")

ispalindrome(string)