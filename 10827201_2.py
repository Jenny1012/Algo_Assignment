# 演算法分析機測
# 學號 : 10827201 | 10827243 | 10827245
# 姓名 : 簡湘媛     | 李筠婷   | 桑怡蓁
# 中原大學資訊工程系

#II. 0-1背包問題 (0-1 Knapsack)

takeItem = list() 
highestValue = 0
def knapsack( value, weight, n, W ) :
    global highestValue 
    c = [ [ 0 for w in range( W + 1 ) ] for i in range( n + 1 ) ]

    for i in range(0,n) :
       for j in range(0,W+1) :
            if ( j - weight[i] < 0 ) :
               c[i+1][j] = c[i][j]
            else :
                if ( c[i][j] > c[i][j - weight[i]] + value[i] ) :
                    c[i+1][j] = c[i][j]
                else :
                    c[i+1][j] = c[i][j - weight[i]] + value[i]

    highestValue = c[n][W]
    i = n-1 
    j = W
    while i >=0 :
        if ( j - weight[i] >= 0 and  c[i+1][j] == c[i][j - weight[i]] + value[i] ) :
            takeItem.append(i+1)
            j = j - weight[i]
        i = i - 1


def ReadInputNum( i ) :
    global inputNum

    try :
        prompt = "Please enter the weight and value for item " + str(i+1) + " : "
        inputNum = list( map( int, input(prompt).split() ) )
        if ( inputNum[0] <= 0 or  inputNum[1] <= 0 ) :
            print( "Please enter positive number.  Try again...")
            ReadInputNum(i)
    except ValueError :
        print("That was no valid number.  Try again...")    
        print()
        ReadInputNum(i)
    return inputNum

weightCorrect = False
while not weightCorrect :
    try :
        knapsack_W = int( input("Please enter knapsack weight W : ") )
        if ( knapsack_W <= 0 ) :
            print("Please enter positive number.  Try again...")  
        else :
            weightCorrect = True
    except ValueError :
        print("That was no valid number.  Try again...")  

numCorrect = False
while not numCorrect :
    try :
        numOfItem = int( input("Please enter num of item N : ") )
        if ( numOfItem <= 0 ) :
            print("Please enter positive number.  Try again...")  
        else :
            numCorrect = True
    except ValueError :
        print("Please enter positive number.  Try again...")  
i = 0 
value = list()
weight = list()
while ( i < numOfItem ) :
    inputNum = ReadInputNum(i)
    weight.append( inputNum[0] )
    value.append(inputNum[1])
    i = i + 1
    
knapsack( value, weight, numOfItem, knapsack_W )
print(highestValue)
i = len(takeItem) - 1
print("Items ", end = "")
while i >= 0 :
    if ( i == 0 ) :
        print( takeItem[i] )
    else :
        print( takeItem[i], end = ", " )
    i = i - 1

