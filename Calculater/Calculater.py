


while True:
	inputData = raw_input("Please input the working equation:")

	a = 0

	operator = None

	for i in inputData:
		if i == "+" or i == "-" or i == "*" or i == "/":
			operator = i
			break
		a = a + 1
		
	str1 = inputData[:a]
			
	str2Len = len(inputData) - len(str1) -1

	str2 = inputData[-str2Len:]
	
			
	x = int(str1,base=10)
	y = int(str2,base=10)

	result = 0


	if operator == "+":
		result = x + y

	if operator == "-":
		result = x - y

	if operator == "*":
		result = x * y

	if operator == "/":
		result = x / y

	print(result)
