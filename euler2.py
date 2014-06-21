#euler2.py
#date: 7 May 2014

def main():
	evenslyst = []
	fibonacci = [1,2]
	n = 1

	while fibonacci[n] < 4000000:
		newNumber = fibonacci[n] + fibonacci[n - 1]
		if newNumber > 4000000:
			break
		elif newNumber % 2 == 0:
			evenslyst.append(newNumber)
		fibonacci.append(newNumber)
		n += 1

	finalSum = adder(evenslyst)
	print("Final sum is: ",finalSum)

def adder(lyst):
	#summation must begin at 2 to account for the two at the beginning of the fibonacci sequence
	summation = 2
	for item in lyst:
		print(item)
		summation += item
	return summation

main()