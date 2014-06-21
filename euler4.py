#euler4.py
#date started: 13 May 2014
#date finished: 13 May 2014

def main():
	palindromes = ["0"]

	for num in range(100,999):
		for num2 in range(100,999):
			temp = str(num * num2)
			if temp == temp[-1::-1]:
				palindromes.append(temp)

	maxItem = findMax(palindromes)

	print(maxItem)

def findMax(ls):
	maxItem = 0
	for item in ls:
		if int(item) > maxItem:
			maxItem = int(item)
	return maxItem

main()