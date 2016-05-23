string = "markov"
array = [5, 3, 1, 4, 2, 0]
newstring = ""

# i = 0
# j = 0
# while i < array.length
# 	while j < array.length
# 		if array[j] == j
# 			newstring += string[j]
# 			puts(newstring)
# 			break
# 		end
# 		j += 1
# 	end
# 	i += 1
# end

# j = 0
# i = 0

# while j < array.length
# 	while i < array.length
# 		if array[i] == j
# 			newstring += string[i]
# 		end
# 		i += 1
# 	end
# 	j += 1
# end
# puts(newstring)

# newarray = []
# i = 0
# while i < array.length
# 	newarray[array[i]] = string[i]
# 	i += 1
# end

# newword = newarray.join

# puts(newword.to_s)

result = ""

  i = 0
  while i < array.length
    result = result + string[array[i]]
    i += 1
  end

  puts(result)