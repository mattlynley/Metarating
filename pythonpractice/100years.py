# num = input("Input a number: ")

# def iseven(num):
	
# 	if num % 4 == 0:
# 		print("Divisible by 4")
# 	elif num % 2 == 0:
# 		print("Even")
# 	else:
# 		print("Odd")

# iseven(num)

num1 = input("Input a number: ")
num2 = input("Input a divisor: ")

def divisor(num1, num2):
	
	if num1 % num2 == 0:
		print("Divides")
	else:
		print("Does not divide")

divisor(num1, num2)