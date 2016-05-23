num1 = 12
num2 = 24

i = 1
newfactor = 1

while i < num2
	if num1 % i == 0 && num2 % i == 0
		newfactor = i
	end
	i += 1
end
puts(newfactor)