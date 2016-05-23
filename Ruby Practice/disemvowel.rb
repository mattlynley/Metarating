word = "elysian"

vowels = ["a", "e", "i", "o", "u"]

newword = ""

truearray = []

i = 0
j = 0
while i < word.length
	j = 0
	while j < vowels.length
		if word[i] == vowels[j]
			truearray[i] = true
		end
		j +=1
	end
	i += 1
end

k = 0
while k < truearray.length
	if truearray[k] != true
		newword += word[k]
	end
	k += 1
end
puts(newword)