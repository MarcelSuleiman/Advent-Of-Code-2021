# link to task: https://adventofcode.com/2021/day/2 

#inputFile = open('input_mini.txt', 'r')
inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

positionX, positionY, aim = 0, 0, 0

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
		#It increases your horizontal position by X units.
		positionY += value

		#It increases your depth by your aim multiplied by X.
		positionX += aim * value

	elif direction == 'down':
		aim += value

	elif direction == 'up':
		aim -= value

#print(f'Depth is {positionX} and distance is {positionY}')
print(positionX*positionY)




	




