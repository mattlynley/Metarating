num = [1, 3, 7, 9, 5]

# reorder the array

# iterate

# find the greatest number



# create a new array with the max at the end

newarray = num

j = 0

while j < 2
	max = newarray.max
	i = 0
	while i < num.length
		if num[i] == max
			newarray[num.length] = max
		else
			newarray[i] = num[i]
		end
		i += 1
	end
	newarray.pop
	j += 1
end

	puts(newarray)