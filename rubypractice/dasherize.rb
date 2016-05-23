num = 134123

word = num.to_s
i = 0
array = []
newword = ""

while i < word.length

	if word[i].to_i % 2 == 0
		array[i] = "even"
	else
		array[i] = "odd"
	end

	i += 1
end

puts(array)

j = 0
newcap = 0

newarray = []

while j < word.length
	newarray[j] = word[j]
	j += 1
end

puts(newarray)

k = 0

while k < array.length
	if array[k] == "odd"
		newword += "-" + newarray[k] + "-"
	else
		newword += newarray[k]
	end
	k += 1
end

if newword[0] == "-"
	newword[0] = ""
end

if newword[newword.length - 1] == "-"
	newword[newword.length - 1] = ""
end

puts(newword)