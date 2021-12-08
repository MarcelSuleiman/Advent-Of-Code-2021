
# link to task: https://adventofcode.com/2021/day/3

#inputFile = open('input_mini.txt')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

cells = [[],[],[],[],[],[],[],[],[],[],[],[]]

for line in lines:

	lineList = list(line) # we get something like this: ['1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '\n']
	del lineList[-1] # we get something like this: ['1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1']

	for elementIndex in range(0, len(lineList)):
		cells[elementIndex].append(lineList[elementIndex])

mostCommonBitGamma = []
mostCommonBitEpsilon = []

for cell in cells:
	if cell.count('0') > cell.count('1'):
		mostCommonBitGamma.append('0')
		mostCommonBitEpsilon.append('1')
	else:
		mostCommonBitGamma.append('1')
		mostCommonBitEpsilon.append('0')

gamma = ''.join(mostCommonBitGamma)
epsilon = ''.join(mostCommonBitEpsilon)

#print(gamma)
#print(epsilon)

gammaDecimal = int(gamma, 2) #int(binary, 2) means: convert to integer - from binary to decimal
epsilonDecimal = int(epsilon, 2) #int(binary, 2) means: convert to integer - from binary to decimal

#print(gammaDecimal)
#print(epsilonDecimal)

print(f'Power consumption of the submarine is: {gammaDecimal*epsilonDecimal}')
