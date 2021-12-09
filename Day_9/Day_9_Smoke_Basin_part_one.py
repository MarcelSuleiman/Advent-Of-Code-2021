
# axis
'''
---------------------------------> X
|
|	When is the man old?
|	When his wet dreams,
|		turn into wet farts.
|
|
|	Kedy je chlap starý?
|	Keď sa jeho mokré sny,
|		zmenia na mokré prdy.
|
|
|
V

Y 

'''

# inputFile = open('input_mini.txt','r')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

ground = []

for line in lines:
	partOfGroud = list(line.replace('\n', ''))
	ground.append(partOfGroud)

numberOfColoumns = len(line)
numberOfRows = len(ground)


def getPussySector(y, x):

	# Central
	if y > 0 and y < numberOfRows-1 and x > 0 and x < numberOfColoumns-1:

		miniSector = []

		point = ground[y][x]

		top = ground[y-1][x]
		right = ground[y][x+1] 
		bottom = ground[y+1][x]
		left = ground[y][x-1]

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		# print(miniSector)
		# print('Central')

		return miniSector

	# Corners 
	# Left Top
	if y == 0 and x == 0:

		miniSector = []

		point = ground[y][x]

		top = 9
		right = ground[y][x+1] 
		bottom = ground[y+1][x]
		left = 9

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# Right Top
	if y == 0 and x == numberOfColoumns-1:

		miniSector = []

		point = ground[y][x]

		top = 9
		right = 9
		bottom = ground[y+1][x]
		left = ground[y][x-1]

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# Left Bottom
	if y == numberOfRows-1 and x == 0:

		miniSector = []

		point = ground[y][x]

		top = ground[y-1][x]
		right = ground[y][x+1]
		bottom = 9
		left = 9

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# Right Bottom
	if y == numberOfRows-1 and x == numberOfColoumns-1:

		miniSector = []

		point = ground[y][x]

		top = ground[y-1][x]
		right = 9
		bottom = 9
		left = ground[y][x-1]

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# Edges
	# left edge

	if y > 0 and y < numberOfRows-1 and x == 0:

		miniSector = []

		point = ground[y][x]

		top = ground[y-1][x]
		right = ground[y][x+1]
		bottom = ground[y+1][x]
		left = 9

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# top edge
	if y == 0 and x > 0 and x < numberOfColoumns-1:

		miniSector = []

		point = ground[y][x]

		top = 9
		right = ground[y][x+1]
		bottom = ground[y+1][x]
		left = ground[y][x-1]

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# right edge
	if y > 0 and y < numberOfRows-1 and x == numberOfColoumns-1:

		miniSector = []

		point = ground[y][x]

		top = ground[y-1][x]
		right = 9
		bottom = ground[y+1][x]
		left = ground[y][x-1]

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector

	# bottom edge
	if y == numberOfRows-1 and x > 0 and x < numberOfColoumns-1:

		miniSector = []

		point = ground[y][x]

		top = ground[y-1][x]
		right = ground[y][x+1]
		bottom = 9
		left = ground[y][x-1]

		miniSector.append(int(point))
		miniSector.append(int(top))
		miniSector.append(int(right))
		miniSector.append(int(bottom))
		miniSector.append(int(left))

		return miniSector


pussySectors = []

for y in range(numberOfRows):	
	for x in range(numberOfColoumns):
		pussySector = getPussySector(y, x)
		pussySectors.append(pussySector)

# print(pussySectors)

riskLevels = []

for pS in pussySectors:
	if pS[0] != 9:
		if pS[0] == min(pS):
			riskLevel = pS[0] + 1
			riskLevels.append(riskLevel)

print(sum(riskLevels))
