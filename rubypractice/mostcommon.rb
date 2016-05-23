word = "abcbab"

i = 0
k = 0
array = []

while i < word.length
	
	if word[i] != array[k]
		array[k] = word[i]
		k += 1
	end


	i += 1
end
puts(array)