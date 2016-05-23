nums = [2,1,5,1,0]

sum = 0
i = 0
n = 0

## start with the first number
## add the next numbers, stop at 7
while sum <= 7
	sum += nums[i+n]
	puts(sum)
	if sum > 7
		sum -= nums[i+n]
		n += 1
	end
	n += 1
end