import re
print('Number:')
creditCardNummber = input().strip()
def luhnValidator(inputVal):
	luhnDigits = []
	luhnnSum = 0
	luhnnStart = 1 if len(creditCardNummber) % 2 else 0
	for index in range(len(inputVal)):
		if((index + 1) % 2 == luhnnStart):
			luhnDigits.append(int(inputVal[index]))
		else:
			weightedDigit = str(int(inputVal[index]) * 2)
			if(len(weightedDigit) == 2):
				weightedDigit = int(weightedDigit[0]) + int(weightedDigit[1])
			luhnDigits.append(weightedDigit)		
	for item in luhnDigits:
		luhnnSum += int(item)
	return (True if str(luhnnSum)[-1] == '0' else False)
if(not luhnValidator(creditCardNummber)):
	print('INVALID')
else:
	creditCardType = None;
	if(re.search('^(34|37)+[0-9]{13}',str(creditCardNummber))):
		creditCardType = 'AMEX'
	elif(re.search('^5[1-5]+[0-9]{14}',str(creditCardNummber))):
		creditCardType = 'MASTERCARD'
	elif(re.search('^4+([0-9]{12}|[0-9]{15}|[0-9]{18})',str(creditCardNummber))):
		creditCardType = 'VISA'
	else:
		creditCardType = 'INVALID'
	print(creditCardType)