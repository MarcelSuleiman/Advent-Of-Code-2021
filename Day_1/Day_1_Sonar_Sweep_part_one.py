import sys

# max value for integer in python -> 9223372036854775807 ==  2^31 - 1
#print(sys.maxsize)

#inputFile = open('input_mini.txt', 'r') # small testing data
inputFile = open('input.txt', 'r') # big final data

lines = inputFile.readlines()

# initial number of measured greater depths
count = 0

# depth one = max, depth two = 0
depth01, depth02 = sys.maxsize, 0

for line in lines:
	depth02 = int(line)

	if depth02 > depth01:
		count += 1
		depth01 = depth02
	else:
		depth01 = depth02

print(count)
