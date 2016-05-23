nums = [0,6,4,1,3,7]

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

k = 0
sum = 0

while k < newarray.length
	sum += newarray[k]
	k += 1
end

puts(sum)