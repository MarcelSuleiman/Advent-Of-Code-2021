import sys

# max value for integer in python -> 9223372036854775807 ==  2^31 - 1
#print(sys.maxsize)

#inputFile = open('input_mini.txt', 'r')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

'''
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
'''

'''
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
'''

#initial number of measured larger depths (sum of three)
count = 0

firstSum, secondSum = sys.maxsize, 0

start, end = 0, 3

for line in lines:
	for element in lines[start:end]:
		secondSum += int(element)

	if secondSum > firstSum:
		count += 1
		start, end = start+1, end+1
		firstSum, secondSum = secondSum, 0
	else:
		start, end = start+1, end+1
		firstSum, secondSum = secondSum, 0

print(count)
