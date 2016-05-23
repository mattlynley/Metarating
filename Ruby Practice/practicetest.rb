nums = [1, 2, 3, 4, 5]

newarray = []

i = 0
j = 0

while i < nums.length
	if nums[i] % 2 != 0
		newarray[j] = nums[i]
		j += 1
	end
	i += 1
end

puts(newarray)

k = 0
sum = 0

while k < newarray.length
	sum += newarray[k]
	k += 1
end

puts(sum)