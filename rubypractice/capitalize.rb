sentence = "this is a sentence"

sentencearray = sentence.split

i = 0

while i < sentencearray.length
	sentencearray[i][0] = sentencearray[i][0].upcase
	puts(sentencearray[i])
	i += 1
end

newarray = sentencearray.join(" ")
puts(newarray)