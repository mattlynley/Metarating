word = "aabdabbc"
i = 0
j = 0
k = 0
repeatcount = 0
wordarray = word.split("")
truearray = []

while i < word.length
	j = i
	while j < word.length
		if word[j] == word[i]
			word[j] = ""
			puts("sliced")
		end
		puts(word)
		j += 1
	end
	i += 1
end