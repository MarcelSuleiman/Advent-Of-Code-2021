'''
this module can create empty 2D array /createEmpty2DArray/ and show you pretify any 2D array /show2DArray/ 
'''

def createEmpty2DArray(size = 1, content = 0):
	'''
	This funfcion creates a 2 dimensional array / list filled with the contents of the variable "content"
	or by 0 (int zero) if content is empty

	size -> length of array and number of rows
	content -> value of each element in array

	function returning completized array
	'''
	emptyList = []

	for i in range(0,size):
		emptyListRow = []
		for j in range(0,size):
			emptyListRow.append(content)

		emptyList.append(emptyListRow)

	return emptyList

def show2DArray(array2D, delimiter = 0):
	'''
	This function print 2D array as grid /map/ line by line

	array2D -> input array
	delimiter -> 1 means only top delimiter, 2 means top and bottom delimiter
	'''
	if delimiter == 1 or delimiter > 1:
		print('-'*len(array2D)*2)

	for line in array2D:
		print(line)

	if delimiter > 1:
		print('-'*len(array2D)*2)

# usage

'''
arrayOne = createEmpty2DArray(10)

arrayTwo = createEmpty2DArray(2, 'A')

arrayThree = createEmpty2DArray(4, ['A', 'B', 'C'])

show2DArray(arrayOne, 1)

show2DArray(arrayTwo, 2)

arrayTwo[1][1] = 'B'

show2DArray(arrayTwo)

show2DArray(arrayThree, 2)

arrayFour = createEmpty2DArray()

show2DArray(arrayFour)
'''
