number = 2

puts(number)

newnum = number % 2.0

puts (newnum)

divnum = number / 2.0

puts(divnum)
if number == 0
	puts("false")
elsif number == 2
	puts("true")
elsif newnum == 0
	if divnum % 2 == 0
		puts("true")
	else
		puts("false")
	end
elsif
	puts("false")
end

puts(2%2)

def is_power_of_two?(num)

	number = num
	
	newnum = number % 2.0
	
	divnum = number / 2.0
	
	if number == 0
		return(false)
	elsif number == 2
		return(true)
	elsif newnum == 0
		if divnum % 2 == 0
			return(true)
		else
			return(false)
		end
	else
		return(false)
	end
end

puts(is_power_of_two?(1))