

def backwards(phrase):

	words = phrase.split()
	length = len(words) - 1
	newwords = []
	i = 0
	while length >= 0:
		newwords.append(words[length])
		length -= 1
	print(" ".join(newwords))

backwards("This is a sentence")