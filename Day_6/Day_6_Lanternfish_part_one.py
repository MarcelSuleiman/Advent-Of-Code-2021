# BRUTE FORCE SOLUTION
# working "fine" only for low day cycle ~ 80-90 days, no more AND only with small data. 

fishesDays = [3,4,3,1,2] # small "testing" input

# big final input
#DELETEthisPREFIX___fishesDays = [5,1,1,3,1,1,5,1,2,1,5,2,5,1,1,1,4,1,1,5,1,1,4,1,1,1,3,5,1,1,1,1,1,1,1,1,1,4,4,4,1,1,1,1,1,4,1,1,1,1,1,5,1,1,1,4,1,1,1,1,1,3,1,1,4,1,4,1,1,2,3,1,1,1,1,4,1,2,2,1,1,1,1,1,1,3,1,1,1,1,1,2,1,1,1,1,1,1,1,4,4,1,4,2,1,1,1,1,1,4,3,1,1,1,1,2,1,1,1,2,1,1,3,1,1,1,2,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,1,1,1,3,1,1,1,1,1,1,2,1,1,2,3,1,2,1,1,4,1,1,5,3,1,1,1,2,4,1,1,2,4,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,4,3,1,2,1,2,1,5,1,2,1,1,5,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,3,1,1,5,1,1,1,1,5,1,4,1,1,1,4,1,3,4,1,4,1,1,1,1,1,1,1,1,1,3,5,1,3,1,1,1,1,4,1,5,3,1,1,1,1,1,5,1,1,1,2,2]


prolog = '''
#********************************************************************************************************
# 												WARNING
#
#		   no more than aprox. 150 days! on my pc 80  days -> 0.2 seconds of runtime,
#												  150 days -> 10 seconds of runtime,
#												  200 days -> still waiting (finally 778.4s)
#
# 									metered on small "testing" input
#					don't try it on big final input with more than 80 days (2 seconds runtime)
#								or :) do it, if you have cold in your room :D
#
#********************************************************************************************************
'''

newFishesDays = []

for day in range(0, 80):
	for fish in range(0, len(fishesDays)):
		fishesDays[fish] -= 1
		if fishesDays[fish] < 0:
			fishesDays[fish] = 6
			fishesDays.append(8)

	#print(fishesDays)

print(len(fishesDays))
