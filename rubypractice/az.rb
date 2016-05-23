word = "lazer"

i = 0
j = 0
len = word.length - 1
truefalse = nil

while i < len
	if word[i] == "a"
		j = i
		while j < (i + 3)
			if word[j] == "z"
				truefalse = true
				break
			end
			j += 1
		end
	end
	i += 1
end

if truefalse == true
	puts("yes")
else
	puts("no")
end