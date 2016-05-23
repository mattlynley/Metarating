def isprime(number)
  if number <= 1
    # only numbers > 1 can be prime.
    return false
  end

  idx = 2
  while idx < number
    if (number % idx) == 0
      return false
    end

    idx += 1
  end

  return true
end

n = 6
i = 0
k = 0

while i < n

	if isprime(k) == true
		i += 1
		newprime = k
	end
	k += 1
end
puts(newprime)