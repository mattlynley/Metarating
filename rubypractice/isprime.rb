number = 2

i = 2
isprime = "true"

while i < number
	if number % i == 0
		isprime = "false"
		break
	end
	i += 1
end

if number == 2
	isprime = "true"
end

puts(isprime)