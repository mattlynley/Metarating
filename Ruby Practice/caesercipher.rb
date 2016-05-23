string = "abc xyz"

i = 0
arraybinary = []
newstring = ""
shiftedarray = []
shiftedarraybasic = []

# while i < string.length
# 	arraybinary[i] = string[i].ord
# 	if arraybinary[i] % 122 >=1
# 		shiftedarray[i] = ((arraybinary[i] % 122) + 97)
# 	else
# 		shiftedarray[i] = (arraybinary[i] + 3)
# 	end
# 	puts(shiftedarray[i])
# 	i += 1
# end

i = 0
offset = 3
arraybinary = []
newstring = ""
shiftedarray = []
shiftedarraybasic = []
while i < string.length
	arraybinary[i] = string[i].ord
	if arraybinary[i] >= (120 - offset)
		shiftedarraybasic[i] = (120 % arraybinary[i]) + (94 + offset)
	else
		shiftedarraybasic[i] = arraybinary[i] + offset
	end
	if shiftedarraybasic[i] < 97
		shiftedarraybasic[i] -= offset
	end
	i +=1
end
j = 0
while j < shiftedarraybasic.length
	shiftedarray[j] = shiftedarraybasic[j].chr
	newstring += shiftedarray[j]
	j += 1
end

puts(newstring)
# j = 0

# while j < arraybinary.length
# 	shiftedarray[j] = (arraybinary[j] + 3)
# 	newstring += shiftedarray[j].chr
# 	puts(newstring)
# 	j += 1
# end

# puts(newstring)