nums = [3, 2, 1, 2, 3, 4]

numbers = nums
i = 0
j = 0
truesum = "false"
positions = []

while j < numbers.length
	i = 0
	while i < numbers.length
		sum = numbers[j] + numbers[i]
		if sum == 0
			positions = [i, j]
			truesum = "true"
		end
		i += 1
	end
	j += 1
end

if positions == []
	puts(nil)
else
	puts(positions)
end