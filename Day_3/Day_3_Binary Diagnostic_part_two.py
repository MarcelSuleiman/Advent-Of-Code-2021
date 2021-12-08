
# link to task: https://adventofcode.com/2021/day/3

#inputFile = open('input_mini.txt', 'r')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

linesOxygen, linesCO2 = lines, lines

def cleaner(cellIndex, cleaningKey, linesGas):
	cleanedList = []

	for line in linesGas:
		if line[cellIndex] == cleaningKey:
			cleanedList.append(line)

	return cleanedList

def walker_Oxygen(cellIndex, linesOxygen):
	zeroCount, oneCount = 0, 0

	for line in linesOxygen:
		if line[cellIndex] == '0':
			zeroCount += 1
		else:
			oneCount += 1

	if zeroCount > oneCount:
		cleaningKey = '0'
	elif zeroCount < oneCount:
		cleaningKey = '1'
	else:
		cleaningKey = '1'

	return cleaningKey

def walker_CO2(cellIndex, linesCO2):
	zeroCount, oneCount = 0, 0

	for line in linesCO2:
		if line[cellIndex] == '0':
			zeroCount += 1
		else:
			oneCount += 1

	if zeroCount < oneCount:
		cleaningKey = '0'
	elif zeroCount > oneCount:
		cleaningKey = '1'
	else:
		cleaningKey = '0'

	return cleaningKey

numOfBits = len(linesOxygen[0])-1 # last bit is "\n" new line. That is why -1 at the end

for cellIndex in range(0, numOfBits):
	if len(linesOxygen) < 2:
		break
	cleaningKeyOxygen = walker_Oxygen(cellIndex, linesOxygen)
	linesOxygen = cleaner(cellIndex, cleaningKeyOxygen, linesOxygen)

for cellIndex in range(0, numOfBits):
	if len(linesCO2) < 2:
		break
	cleaningKeyCO2 = walker_CO2(cellIndex, linesCO2)
	linesCO2 = cleaner(cellIndex, cleaningKeyCO2, linesCO2)

#print(linesOxygen, linesCO2)
#print(linesOxygen[0][0:numOfBits], linesCO2[0][0:numOfBits])

#		integer(binary, decimal)
#		int(binary, 2) means: convert to integer from binary to decimal

#result = int(linesOxygen[0][0:numOfBits], 2) * int(linesCO2[0][0:numOfBits], 2)
result = int(linesOxygen[0], 2) * int(linesCO2[0], 2)

print(result)
