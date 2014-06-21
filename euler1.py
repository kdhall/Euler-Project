#Author: Kyle Hall
#Title: Project Euler problem 1
#Date: 7 May 2014

def main():
	intlyst = []

	for i in range (1000):
		if i % 3 == 0:
			intlyst.append(i)
		elif i % 5 == 0:
			intlyst.append(i)
		else:
			continue

	totalNumber = 0
	finalSum = 0		

	for item in intlyst:
		totalNumber += 1
		finalSum += item

	print("Total number of integers less than 1000 which are divisible by 3 or 5: ",totalNumber)
	print("Summation of all these integers: ",finalSum)

main()

#this code was correct on the first try