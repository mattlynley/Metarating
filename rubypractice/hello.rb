string = "abc"

def reverse(string)
	stringlength = string.length
	stringsplit = string.split
	newstring = ""
	i = 0
	while i < stringlength
		newstring + stringsplit[i]
	end

end

puts(reverse(string))