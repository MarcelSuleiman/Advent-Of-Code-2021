# link to task: https://adventofcode.com/2021/day/2 

#inputFile = open('input_mini.txt', 'r')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

positionX, positionY = 0, 0

'''
0,0
	--------------> Y
	|
	|	>ooo>
	|
	|
	|
	V

	X
'''

for line in lines:
	direction, value = line.split(' ')[0], int(line.split(' ')[1])

	if direction == 'forward':
		positionY += value
	elif direction == 'down':
		positionX += value
	elif direction == 'up':
		positionX -= value

#print(f'Depth is {positionX} and distance is {positionY}')
print(positionX*positionY)
