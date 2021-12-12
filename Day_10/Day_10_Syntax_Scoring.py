# link to task: https://adventofcode.com/2021/day/10/input

inputFile = open('input.txt', 'r')

lines = inputFile.readlines()

navigationSubsystem = []
linesWithSyntaxError = []

for line in lines:
	part = line.replace('\n', '')
	navigationSubsystem.append(list(part))

scoreDic = {')':3,
			']':57,
			'}':1197,
			'>':25137}

chunkOperatorsOpen = ['(', '[', '{', '<']
chunkOperatorsClose = [')', ']', '}', '>']

pairs = ['()','[]','{}','<>']
brokenPairs = ['(]','(}','(>','[)','[}','[>','{)','{]','{>','<)','<]','<}']

finalScore = 0

assistList = []

for line in navigationSubsystem:
	print(line)
	for element in line:
		
		if element in chunkOperatorsOpen:
			assistList.append(element)

		if element in chunkOperatorsClose:

			if assistList[-1]+element in pairs:
				assistList.pop(-1)
			
			elif assistList[-1]+element in brokenPairs:
				finalScore += scoreDic[element]
				break

print(finalScore)







