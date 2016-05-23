

vowels = ["a", "e", "i", "o", "u"]
puts(vowels)

word = "increase"
puts(word)
puts(word[2])

k = 0
m = 0
vowelcount = 0

while k < word.length
	while m < vowels.length
		if word[k] == vowels[m]
			vowelcount += 1
		end
		m += 1
	end
	k += 1
	m = 0
end
puts (vowelcount)