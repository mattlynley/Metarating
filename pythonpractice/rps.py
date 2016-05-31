

def RPSwinner():
	
	while True:

		play1 = raw_input("Enter RPS: ")
		play2 = raw_input("Enter RPS: ")
		playarray = [play1, play2]
		playerwinnner = [False, False]

		
		if 'R' and 'S' in playarray:
			print("Rock and scissors are in there")
			break
		elif 'S' in playarray: 
			print("Scissors is in there")
			break

RPSwinner()