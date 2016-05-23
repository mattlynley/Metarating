word = "racecar"

newword = ""
stringlength = word.length - 1

while stringlength >= 0
	puts(word[stringlength])
	newword += word[stringlength].to_s
	stringlength -= 1
end

if newword == word
	puts("yep")
else
	puts("nope")
end