# link to task: https://adventofcode.com/2021/day/7 

import sys

#inputFile = open('input_mini.txt', 'r')
inputFile = open('input.txt', 'r') 

lines = inputFile.readlines()

linesList = list(lines[0].split(',')) # split 1 string value ('1101,1,29,67,1102,0,1,65,....') in to many separate values

positionListInt = []

for element in linesList:
	positionListInt.append(int(element)) # we gradually fill array / list with the values converted to a number (int)

# brute force solution

# find min and max position
# I do not know where the ideal position will be but 100% between these values
minPosition = min(positionListInt)
maxPosition = max(positionListInt)

'''
If you feel that one of the crabs could have managerial manners, 
and you have strong concerns that he might say, "Are we sure?"
meeting at 13:00 prepare your documents
(excel, of course)
we will go through it.
... You know ... 
Uncomment the lines: 34-37, 55, 56, 58
'''

#exportFile = 'fuel_consumed.csv'
#file = open(exportFile, "a")
#head = 'Position' + ';' + 'Used fuel' + ';'
#file.write(head + '\n')

fuel_consumed = []

for i in range(0, len(positionListInt)+1):

	dataElement = []

	potencionalBestPosition = i
	usedFuel = 0

	for element in positionListInt:
		usedFuel += abs(element - potencionalBestPosition)

	dataElement.append(potencionalBestPosition)
	dataElement.append(usedFuel)
	fuel_consumed.append(dataElement)

	#text = str(potencionalBestPosition) + ';' + str(usedFuel) + ';'
	#file.write(text + '\n')
	
#file.close()

lowestValue = sys.maxsize
index = 0

for element in fuel_consumed:
	selectedValue = element[1]

	if selectedValue < lowestValue:
		lowestValue = selectedValue
		indexFinal = index

	index += 1

print(f'The least fuel {lowestValue} is consumed\nif all crabs move into position {indexFinal}')
