string = "dabcbaefghijihgfe"

def palindrome?(string)
  i = 0
  while i < string.length
    if string[i] != string[(string.length - 1) - i]
      return false
    end

    i += 1
  end

  return true
end

j = 0
k = 1
pallength = 0

while j < string.length
	k = 1
	while k <= string.length
		sliced = string.slice(j,k)
		puts(sliced)
		if palindrome?(sliced) == true && sliced.length > pallength
			pallength = sliced.length
		end
		k += 1
	end
	j += 1
end
puts(pallength)