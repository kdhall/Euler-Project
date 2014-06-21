#euler5.py
#date started: 13 May 2014

import time

def main():
	done = False
	n = 1

	start_Time = time.clock()

	while done != True	:
		for i in range(1,21):
			if n % i != 0:
				n += 1
				break
			if i == 20:
				done = True

	end_time = time.clock()

	elapsed_time = end_time - start_Time

	print(n)
	print(elapsed_time)

main()
