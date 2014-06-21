#euler6.py

def main():
	sumOfSq = sumOfSquares()
	squaredSum = squareOfSum()

	print(squaredSum)
	print(sumOfSq)
	print(squaredSum - sumOfSq)

def sumOfSquares():
	total = 0
	for i in range(1,101):
		temp = i * i
		total += temp

	return total

def squareOfSum():
	total = 0
	for i in range(1,101):
		total += i

	total = total * total

	return total

main()
