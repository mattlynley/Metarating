# string = "hello sweetie dear goodness"

# stringsplit = string.split

# puts(stringsplit)

# arraylength = stringsplit.length

# puts(arraylength)

# puts(stringsplit[0])

# newarray = []

# i = 0

# while i < arraylength
# 	puts(stringsplit[i])
# 	newarray[i]=stringsplit[i].length
# 	puts(newarray[i])
# 	i = i + 1
# end

# k = 0
# i = 0

# while i < newarray.length
# 	if newarray[i] > k
# 		k = newarray[i]
# 	end
# 	i = i + 1
# end


# puts(k)
sentence = "goodness whattheheck theres my sweetie"

	stringsplit = sentence.split
	arraylength = stringsplit.length
	
	newarray = []
	
	i = 0
	
	## get an array of lengths

	while i < arraylength
		newarray[i]=stringsplit[i].length
		i = i + 1
	end

	alength=newarray.length

	i = 0

	# while i < alength
	# 	puts(newarray[i])
	# 	i = i + 1
	# end
	
	i = 0
	k = 0
	j = 0

	while i < alength

		if newarray[i] > k
			k = newarray[i]
			j = i
		end

		i = i + 1
	end
	
	return(stringsplit[j])
	
# 	## pick the slot to return

# 	while i < alength

# 		## check if new # is larger

# 		if newarray[i] > k

# 			## if larger, change it

# 			k = i

# 		end
# 		## iterate

# 		i = i + 1

# 	end
# puts(stringsplit[k])