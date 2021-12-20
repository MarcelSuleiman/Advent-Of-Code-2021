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

# added for par two
correctNavigationSubsystem = []

# added for par two
# counting line
lineCount = 0

for line in navigationSubsystem:
	
	# added for par two
	# add line to new correct subsystem , next we delete incorrect line
	correctNavigationSubsystem.append(line)

	assistList = []
	
	for element in line:
		
		if element in chunkOperatorsOpen:
			assistList.append(element)

		if element in chunkOperatorsClose:

			if assistList[-1]+element in pairs:
				assistList.pop(-1)
			
			elif assistList[-1]+element in brokenPairs:
				finalScore += scoreDic[element]

				# added for par two
				# erase broken line
				correctNavigationSubsystem.pop(-1)
				break

	# added for par two
	# counting line
	lineCount += 1

print(finalScore)

# ---- part two


scoreDic2 = {')':1,
			']':2,
			'}':3,
			'>':4}


totalScoreAllInList = []

for line in correctNavigationSubsystem:
	assistList = []

	for element in line:
		
		if element in chunkOperatorsOpen:
			assistList.append(element)

		if element in chunkOperatorsClose:

			if assistList[-1]+element in pairs:
				assistList.pop(-1)

	assistListReverse = assistList
	assistListReverse.reverse()

	workingString = ''

	for char in assistListReverse:
		workingString += char

	finalString = workingString.replace('(', ')').replace('[', ']').replace('{', '}').replace('<', '>')

	finalStringList = list(finalString)

	totalScore = 0

	for e in finalString:
		totalScore = totalScore * 5
		totalScore += scoreDic2[e]

	totalScoreAllInList.append(totalScore)

totalScoreAllInList.sort()

middleScore = len(totalScoreAllInList) // 2
print(totalScoreAllInList[middleScore])















