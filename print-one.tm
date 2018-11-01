0: LDA 6,1(7)	# store return address for main
1: LDA 7,<main>(0)	# jump to main
2: LDA 6,1(7)	# store return address for PRINT
3: LDA 7,<print>(0)	# jump to PRINT
4: HALT 0,0,0	# 
*
*PRINT
*
	# print value in r5
5: OUT 5,0,0	# 
6: LDA 7,0(6)	# return to call
*
*main
*
7: LDC 5,1(0)	# load 1 into r5
8: ADD 4,0,5	# move return value to r4
9: LDA 7,0(6)	# load return address into r7
