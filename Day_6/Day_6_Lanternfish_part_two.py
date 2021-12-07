# link to task: https://adventofcode.com/2021/day/6

# Better solution

#baseFishesDays = [3,4,3,1,2]
baseFishesDays = [5,1,1,3,1,1,5,1,2,1,5,2,5,1,1,1,4,1,1,5,1,1,4,1,1,1,3,5,1,1,1,1,1,1,1,1,1,4,4,4,1,1,1,1,1,4,1,1,1,1,1,5,1,1,1,4,1,1,1,1,1,3,1,1,4,1,4,1,1,2,3,1,1,1,1,4,1,2,2,1,1,1,1,1,1,3,1,1,1,1,1,2,1,1,1,1,1,1,1,4,4,1,4,2,1,1,1,1,1,4,3,1,1,1,1,2,1,1,1,2,1,1,3,1,1,1,2,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,1,1,1,3,1,1,1,1,1,1,2,1,1,2,3,1,2,1,1,4,1,1,5,3,1,1,1,2,4,1,1,2,4,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,4,3,1,2,1,2,1,5,1,2,1,1,5,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,3,1,1,5,1,1,1,1,5,1,4,1,1,1,4,1,3,4,1,4,1,1,1,1,1,1,1,1,1,3,5,1,3,1,1,1,1,4,1,5,3,1,1,1,1,1,5,1,1,1,2,2]

		# indexes    0, 1, 2, 3, 4, 5, 6 ,7 ,8
allFischesByDays_TEMPLATE = [0, 1, 1, 2, 1, 0, 0, 0, 0]
allFischesByDays =	    [0, 0, 0, 0, 0, 0, 0, 0, 0]

for day in range(0,9):
	sumOfFisches = baseFishesDays.count(day)
	allFischesByDays[day] += sumOfFisches

for day in range(0, 256):
	resetedAndNewBornFisches = [0,0]
	shiftedFisches = [0,0,0,0,0,0,0,0,0]

	for fishIndex in range(len(allFischesByDays)):
		if fishIndex == 0:
			resetedAndNewBornFisches[0] = allFischesByDays[0]
			resetedAndNewBornFisches[1] = allFischesByDays[0]

		elif fishIndex > 0:
			allFischesByDays[fishIndex-1] = allFischesByDays[fishIndex]

	#allFischesByDays[8] = 0 # not nessesery, just for feeling good

	for i in range(len(resetedAndNewBornFisches)):
		if i == 0:
			allFischesByDays[6] += resetedAndNewBornFisches[0] # 6d
		elif i == 1:
			allFischesByDays[8] = resetedAndNewBornFisches[1] # 8d
	
	# Only for visual inspection
	#print(f'		 0, 1, 2, 3, 4, 5, 6, 7, 8 ')
	#print(f'Day: {day}. {allFischesByDays}')
	#print()

#print(allFischesByDays)
print(sum(allFischesByDays))
