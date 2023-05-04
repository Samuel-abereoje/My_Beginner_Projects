def add(a, b): 
		answer = a + b
		print("Your answer is: ", answer, "\n")
	
def sub(a, b):
		answer = a - b
		print("Your answer is: ", answer)
	
def mul(a, b):
		answer = a * b
		print("Your answer is: ", answer)
	
def div(a, b):
		answer = a / b
		print("Your answer is: ", answer)
		
while True:
	print ("choose an operator" "\n")
	print ("A for Addition")
	print ("S for subtraction")
	print ("M for Multiplication")
	print ("D for Division")
	print ("Q for quit" + "\n") 
	opp = input("Enter desired operator: ")
	
	if opp == 'A' or opp == 'a':
		a = int(input ("Enter first digit: "))
		b = int(input ("Enter second digit: "))
		add(a, b)
	
	elif opp == "S" or opp =='s':
		a = int(input ("Enter first digit: "))
		b = int(input ("Enter second digit: "))
		sub(a, b)
				
	elif opp == "M" or opp =='m':
		a = int(input ("Enter first digit: "))
		b = int(input ("Enter second digit: "))
		mul(a, b)
				
	elif opp == "D" or opp =='d':
		a = int(input ("Enter first digit: "))
		b = int(input ("Enter second digit: "))
		div(a, b)
				
	elif opp == "Q" or opp =='q':
		quit()
				
	else:
			print ("print invalid syntax")