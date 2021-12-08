# link to task: https://adventofcode.com/2021/day/7 

import sys

#inputFile = open('input_mini.txt', 'r')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

linesList = list(lines[0].split(','))

positionListInt = []

for element in linesList:
	positionListInt.append(int(element))

# brute force solution

# find min and max position
# I do not know where the ideal position will be but 100% between these values
minPosition = min(positionListInt)
maxPosition = max(positionListInt)

# If you want excel (CSV) datasheet for presentation or somethig else
# uncomment lines 27-30, 64-67

#exportFile = 'fuel_consumed_exponential.csv'
#file = open(exportFile, "a")
#head = 'Position' + ';' + 'Used fuel' + ';'
#file.write(head + '\n')

fuel_consumed = []

for i in range(minPosition,maxPosition+1):

	dataElement = []

	#print(f'We count the position: {i}')
	usedFuelTotal = 0
	potencionalBestPosition = i

	for element in positionListInt:
		usedFuelOneCrab = 0
		distance = abs(element - potencionalBestPosition)

		#Visually easier to understand, but slower [Finished in 235.4s] ~ 4 minutes
		'''
		for f in range(1, distance+1):
			usedFuelOneCrab += f
		'''

		# quicklier than previous solution and make the same
		usedFuelOneCrab = sum(list(range(1, distance+1))) # [Finished in 47.4s] ~ 1 minute

		usedFuelTotal += usedFuelOneCrab

	# fill array [potencionalBestPosition, usedFuelTotal]
	dataElement.append(potencionalBestPosition)
	dataElement.append(usedFuelTotal)

	# fill 2Darray by [[potencionalBestposition1, usedFuelTotal1], [potencionalBestposition1, usedFuelTotal1], ...]
	fuel_consumed.append(dataElement)

	#text = str(potencionalBestPosition) + ';' + str(usedFuelTotal) + ';'
	#file.write(text + '\n')

#file.close()

# finding lowest value (fuel consumed) and tracking position
lowestValue = sys.maxsize
index = 0

for element in fuel_consumed:
	selectedValue = element[1]

	if selectedValue < lowestValue:
		lowestValue = selectedValue
		indexFinal = index

	index += 1

print(f'The least fuel {lowestValue} is consumed\nif all crabs move into position {indexFinal}')
