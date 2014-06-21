#euler3.py
#date started: 12 May 2014

def main():
	x = greatestPrimeFactor(600851475143)
	print(x)

def greatestPrimeFactor(n):
	factorList = []
	nextFactor = divider(n)
	
	while n != 1:
		
		if nextFactor == -1:
			print("Not divisible by 2-100.")
			return -1
		else:
			n = n // nextFactor
			factorList.append(nextFactor)

	maxItem = findMax(factorList)
	return maxItem
	
def divider(num):
	for x in range(2,100):
		if num % x == 0:
			return x
	return -1

def isPrime(integer):
	for i in range(2,10):
		if integer % i == 0:
			return False
	return True

def findMax(lyst):
	maxItem = 0
	for i in range(len(lyst)):
		temp = lyst[i]
		if temp > maxItem:
			maxItem = temp

	return maxItem

main()