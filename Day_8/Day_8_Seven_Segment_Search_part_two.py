h = '''
  0:      1:      2:      3:      4:
 aaaa            aaaa    aaaa        
b    c       c       c       c  b    c
b    c       c       c       c  b    c
                 dddd    dddd    dddd
e    f       f  e            f       f
e    f       f  e            f       f
 gggg            gggg    gggg        

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b       b            c  b    c  b    c
b       b            c  b    c  b    c
 dddd    dddd            dddd    dddd
     f  e    f       f  e    f       f
     f  e    f       f  e    f       f
 gggg    gggg            gggg    gggg

'''


inputFile = open('input.txt', 'r')

'''
bceadfg ebcdaf gdaecf fgcaeb fdbea fcdea cbda begdf afb ba | acfbeg cbfgea gebacf ab
bg dfcba agedcb dfgab agb cafedgb gfdea ceafdg bfgade gbef | befg gafde dafbg cfbadeg
fg befdc afecdbg gbf gfcdab cfge cbdfeg efbdg baegd deafcb | bgf edfbac ebgdf fgb
'''

lines = inputFile.readlines()

finalStringNums = []
finalIntegerNums = []

for line in lines:
	splitedLine = line.split(' | ')
	inputKey = splitedLine[0].split(' ')
	outputKey = splitedLine[1].replace('\n', '').split(' ')
	
	oneStringDigit = twoStringDigit = treeStringDigit = fourStringDigit = fiveStringDigit = sixStringDigit= sevenStringDigit = eightStringDigit = nineStringDigit = zeroStringDigit = ''

	index = 0
	valueList = []

	for key in inputKey:


		# only 1 digit use 2 segments -> number one. Any string with length 2 is 1
		# only 1 digit use 3 segments -> number seven. Any string with length 3 is 7
		# only 1 digit use 4 segments -> number four. Any string with length 4 is 4
		# only 1 digit use (all) 7 segments -> number eight. Any string with length 7 is 8

		if len(key) == 2:
			oneStringDigit = '1'
			oneString = key
			oneChars = list(key)
			#print(f'I found number one: {oneChars}')
			valueList.append(key)

		if len(key) == 3:
			sevenStringDigit = '7'
			sevenString = key
			sevenChars = list(key)
			#print(f'I found number seven: {sevenChars}')
			valueList.append(key)

		if len(key) == 4:
			fourStringDigit = '4'
			fourString = key
			fourChars = list(key)
			#print(f'I found number four: {fourChars}')
			valueList.append(key)

		if len(key) == 7:
			eightStringDigit = '8' 
			eightString = key
			eightChars = list(key)
			#print(f'I found number eight: {eightChars}')
			valueList.append(key)

		if oneStringDigit != '' and sevenStringDigit != '' and fourStringDigit != '' and eightStringDigit != '':
				break

		index += 1

	# from now, we dont need them in keyList

	for element in valueList:
		inputKey.remove(element)

	for key in inputKey:
		# we are looking for number 3.
		# no. 3 has 5 chars -> string must by: len(string) == 5
		# in this string must be all chars from digit 1 

		if len(key) == 5:
			if oneChars[0] in key and oneChars[1] in key:
				# it is no. 3
				treeStringDigit = '3'
				treeString = key
				treeChars = list(key)
				#print(f'I found number three: {treeChars}')

	inputKey.remove(treeString)

	for key in inputKey:
		# we are looking for number 9.
		# no. 9 is string of number 3 -> 5chars + 1 char = 6 chars
		# because "9" have 6 lights segments

		if len(key) == 6:
			if treeChars[0] in key and treeChars[1] in key and treeChars[2] in key and treeChars[3] in key and treeChars[4] in key:
				# it is no. 9
				nineStringDigit = '9'
				nineString = key
				nineChars = list(key)
				#print(f'I found number nine: {nineChars}')

	inputKey.remove(nineString)

	for key in inputKey:
		# we are looking for number 0.
		# no. 0 is string with length 6 and must include chars from one
		# like number 9 but we foud number 9 and removed it from list

		if len(key) == 6:
			if oneChars[0] in key and oneChars[1] in key:
				# it is no. 0
				zeroStringDigit = '0'
				zeroString = key
				zeroChars = list(key)
				#print(f'I found number zero: {zeroChars}')

	inputKey.remove(zeroString)

	for key in inputKey:
		# we are looking for number 6.
		# last string who has length 6 ;) we found 9 (cuted of), 0 (cuted of) 
		# now we must have only one 6-length string in our list

		if len(key) == 6:
			# it is no. 6
			sixStringDigit = '6'
			sixString = key
			sixChars = list(key)
			#print(f'I found number six: {sixChars}')

	inputKey.remove(sixString)

	# hmm, finally we have 2 string coresponding to numbers: 2 and 5
	# who is who?

	# if we know number 1 has 2 chars (like AB/BA)
	#			 number 6 do not include one of 2 chars from digit 1 (like A or B)
	#
	# number 5 must have length 5 chars without one char of oneChars
	# but which one?

	# if we look at number six (char format) we must find, which par of "one" is inside of "six"
	# that char representing "bottom part" of "one".
	# if we want identify no 5,  
	# we are looking for string with bottom part of "one", OR, without upper part of "one"

	for char in oneChars:
		if char in sixChars:
			for key in inputKey:
				if char in key:
					# it is no. 5
					fiveStringDigit = '5'
					fiveString = key
					fiveChars = list(key)
					#print(f'I found number five: {fiveChars}')

	inputKey.remove(fiveString)

	# "finally" last string is our last unknow number. Number 2

	twoStringDigit = '2'
	twoString = inputKey[0]
	twoChars = list(inputKey[0])
	#print(f'I found number two: {twoChars}')

	inputKey.remove(twoString)

	# second part
	# we must decrypt 4 numbers by our keys 

	# ''.join(sorted(string))

	finalStringNumber = ''

	for hiddenNumber in outputKey:

		if ''.join(sorted(hiddenNumber)) == ''.join(sorted(oneString)):
			finalStringNumber += oneStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(twoString)):
			finalStringNumber += twoStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(treeString)):
			finalStringNumber += treeStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(fourString)):
			finalStringNumber += fourStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(fiveString)):
			finalStringNumber += fiveStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(sixString)):
			finalStringNumber += sixStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(sevenString)):
			finalStringNumber += sevenStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(eightString)):
			finalStringNumber += eightStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(nineString)):
			finalStringNumber += nineStringDigit

		elif ''.join(sorted(hiddenNumber)) == ''.join(sorted(zeroString)):
			finalStringNumber += zeroStringDigit

	finalIntegerNums.append(int(finalStringNumber))

#for i in range(len(finalStringNums)):
	#print(f'{finalIntegerNums[i]}')

print(f'Sum of hidden numbers on right side is: {sum(finalIntegerNums)}')