array = [1,2,4,1,4]
sum = 0
i = 0
j = 0
luckyseven = false
while i < array.length - 2
	j = i
	while j < i + 3
		sum += array[j]
		j += 1
	end
	if sum == 7
		luckyseven = true
		sum = 0
	else
		sum = 0
	end
	i += 1
end

puts(luckyseven)