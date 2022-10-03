# 演算法分析機測
# 學號 : 10827201 | 10827243 | 10827245
# 姓名 : 簡湘媛     | 李筠婷   | 桑怡蓁
# 中原大學資訊工程系

# I. 最長共同子序列 (Longest Common Subsequence)

from msilib import sequence
import re

def LCS( X, Y ):

	UPPERLEFT = 1
	UP 		  = 2
	LEFT 	  = 3

	m = len( X )
	n = len( Y )

	c = [ [ 0 for j in range( 0, n + 1 ) ] for i in range( 0, m + 1 ) ]
	b = [ [ 0 for j in range( 0, n + 1 ) ] for i in range( 0, m + 1 ) ]
	
	for i in range( 1, m + 1 ):
		c[i][0] = 0
	
	for j in range( 1, n + 1 ):
		c[0][j] = 0
	
	for i in range( 1, m + 1 ):
		for j in range( 1, n + 1 ):
			if X[i - 1] == Y[j - 1]:
				c[i][j] = c[i - 1][j - 1] + 1
				b[i][j] = UPPERLEFT
			else:
				if c[i - 1][j] >= c[i][j - 1]:
					c[i][j] = c[i - 1][j]
					b[i][j] = UP
				else:
					c[i][j] = c[i][j - 1]
					b[i][j] = LEFT
	
	i = m
	j = n
	result = ""
	while i != 0 and j != 0:  
		if b[i][j] == UPPERLEFT:
			result = str( X[i - 1] ) + result
			i -= 1
			j -= 1
		elif b[i][j] == UP:
			i -= 1
		else:
			j -= 1

	return result


#  1 <= m、 n <= 100 
def ReadInputNum() :
    global inputNum

    try :
        inputNum = list( map( int, input("Please enter the num of sequence1 and sequence2: ").split() ) )
        if ( (inputNum[0] == 0 and inputNum[1] != 0 ) or ( inputNum[0] != 0 and inputNum[1] == 0 )) :
            print( "Please enter range in [1,100].  Try again...")
            ReadInputNum()		
        if ( inputNum[0] < 0 or inputNum[0] > 100 or  inputNum[1] < 0 or inputNum[1] > 100 ) :
            print( "Please enter range in [1,100].  Try again...")
            ReadInputNum()
    except ValueError :
        print("That was no valid number.  Try again...")    
        print()
        ReadInputNum()
    return inputNum

inputNum = ReadInputNum()
numOfsequence1 = inputNum[0]
numOfsequence2 = inputNum[1]

casenum = 0
while ( numOfsequence1 != 0 or  numOfsequence2 != 0 ) :
	casenum = casenum + 1
	sequence1 = list()
	sequence2 = list()

	correct = False 
	print( "Please enter sequence1 : ") #字元為英文的大寫或小寫
	while ( not correct ) :
		sequence1 = input()
		sequence1 = re.sub(r"[\n\t\s]*", "", sequence1)
		if ( len(sequence1) != numOfsequence1 ) :
			print( "Num of sequence1 is not correct !! Try again.")
		elif ( not sequence1.isalpha() ):
			print( "Please enter English letter!! Try again.")
		else :
			correct = True

	correct = False 
	print( "Please enter sequence2 : ")
	while ( not correct ) :
		sequence2 = input()
		sequence2 = re.sub(r"[\n\t\s]*", "", sequence2)
		if ( len(sequence2) != numOfsequence2 ) :
			print( "Num of sequence2 is not correct !! Try again.")
		elif ( not sequence2.isalpha() ):
			print( "Please enter English letter!! Try again.")
		else :
			correct = True

	lcs = LCS( sequence1, sequence2 )
	print( "Case #", casenum )
	print( "Length of LCS = ", len(lcs) )
	print( "LCS = ", lcs )

	inputNum = ReadInputNum()
	numOfsequence1 = inputNum[0]
	numOfsequence2 = inputNum[1]
	
