# 演算法分析機測
# 學號 : 10827201 | 10827243 | 10827245
# 姓名 : 簡湘媛     | 李筠婷   | 桑怡蓁
# 中原大學資訊工程系

# IV. 單一源 最短路徑問題 (Single-Source Shortest Paths Problem)

from ftplib import all_errors
from typing import List
import re
import copy

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        movePath = []
        dire = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'T':   # 目標位置
                    T = (i, j)
                elif grid[i][j] == 'B': # 箱子的初始位置
                    B = (i, j)
                elif grid[i][j] == 'S': # 人的初始位置
                    S = (i, j)

        def check1(x, y):
            return x >= 0 and x < r and y >= 0 and y < c and grid[x][y] != '#'

        def canMoveTo(e, b, q, vis): # e : 人要移到的位置 
            global pRoute
            pRoute.clear()
            while q:
                pW_copy = []
                pre, pW = q.pop(0) # pre : 人原本在的位置, pW:人移動的路徑
                if pre == e:
                    #print(pW_copy)
                    pRoute = copy.deepcopy(pW)
                    return True

                for i, j in dire:
                    pW_copy = copy.deepcopy(pW)
                    nx, ny = pre[0] + i, pre[1] + j
                    if check1(nx, ny) and \
                        (nx, ny) != b and (nx, ny) not in vis:

                        if ( i == 0 and j == 1 ) :
                            pW_copy.append('e')
                        elif ( i == 0 and j == -1 ) :
                            pW_copy.append('w')
                        elif ( i == -1 and j == 0 ) :
                            pW_copy.append('n')
                        elif ( i == 1 and j == 0 ) :
                            pW_copy.append('s')

                        q.append(((nx, ny), pW_copy))
                        vis.add((nx, ny))

            return False

        def move(e, q, vis): # e : 目標位置   q:目前箱與人的位置  vis : 箱與人走過的位置
            global allPath
            res = 0
            
            while q:

                for _ in range(len(q)): #
                    b, p, w = q.pop(0) # b箱子的位置, p人在的位置

                    if b == e: # 是否為目標位置
                        allPath = copy.deepcopy(w)
                        print("allPath :", allPath)                        
                        return res
                    
                    for i, j in dire: #右左上下依序走

                        w_copy = copy.deepcopy(w)
                        nx, ny = b[0] + i, b[1] + j
                        pMove = []
                        if check1(nx, ny) and \
                            check1(b[0] - i, b[1] - j) and\
                            ((nx, ny), b) not in vis and \
                            canMoveTo((b[0] - i, b[1] - j), b, [(p, pMove)], set([p])):

                            for path in(pRoute) :
                               w_copy.append(path)
                            if ( i == 0 and j == 1 ) :
                                w_copy.append('E')
                            elif ( i == 0 and j == -1 ) :
                                w_copy.append('W')
                            elif ( i == -1 and j == 0 ) :
                                w_copy.append('N')
                            elif ( i == 1 and j == 0 ) :
                                w_copy.append('S')          

                            q.append(((nx, ny), b, w_copy))
                            vis.add(((nx, ny), b))



                res += 1
            return -1

        return move(T, [(B, S, movePath )], set([(B, S)]))


def ReadInputNum() :
    global inputNum

    try :
        inputNum = list( map( int, input("Please enter the num of row and coulmn: ").split() ) )
        if ( (inputNum[0] == 0 and inputNum[1] != 0 ) or ( inputNum[0] != 0 and inputNum[1] == 0 )) :
            print( "Please enter range in [1,20].  Try again...")
            ReadInputNum()		
        if ( inputNum[0] < 0 or inputNum[0] > 20 or  inputNum[1] < 0 or inputNum[1] > 20 ) :
            print( "Please enter range in [1,20].  Try again...")
            ReadInputNum()
    except ValueError :
        print("That was no valid number.  Try again...")    
        print()
        ReadInputNum()
    return inputNum

def FindListElement( str, c ) :
    try :
        str.index(c)
        return True
    except ValueError :
        return False  

inputNum = ReadInputNum()
row = inputNum[0]
column = inputNum[1]

mazeNum = 0
pRoute = []
allPath = []

while ( row != 0 or  column != 0 ) :
    allPath.clear()
    
    hasStart = False
    hasBox = False
    hasTarget = False
    maze = [ [0 for i in range(column)] for j in range(row)]
    print("Please Enter", row, "*", column ,"maze" )

    for i in range(row) :
        
        isCorrect = False
        while not isCorrect :
            str= input()

            if ( len(str) != column ) :
                print( "Num of column is not correct !! Try again.")
                continue
            elif FindListElement( str, 'S' ) and hasStart :
                print( "It's already have Start vertex !! Try again.")
                continue
            elif FindListElement( str, 'B' ) and hasBox :
                print( "It's already have Box vertex !! Try again.")
                continue
            elif FindListElement( str, 'T' ) and hasTarget :
                print( "It's already have Target vertex !! Try again.")
                continue
            
            error = False
            for c in str :
                if c != 'S' and c != 'B' and c != 'T' and c != '.' and c != '#' :
                    error = True
                    print("It can only be \{S, B, T, ., # \} !! Try again.")
                    break

            if error :
                continue
            else :
                isCorrect = True
                if FindListElement( str, 'S' )  :
                    hasStart = True
                if FindListElement( str, 'B' )  :
                    hasBox = True
                if FindListElement( str, 'T' ) :
                    hasTarget = True
        
                for j in range(column) :
                    maze[i][j] = str[j]
        #str = re.sub(r"[\n\t\s]*", "", str)
    
    if (not hasStart) or (not hasBox) or (not hasTarget) :
        print(hasStart, hasBox, hasTarget)
        print("Error Maze!!!! Try again.")
        continue
    
    #print(maze)
    M = Solution()
    move = M.minPushBox(maze)
    mazeNum = mazeNum + 1
    print( "Maze #", mazeNum )
    if move == -1 :
        print("Impossible")
    else :
        for p in allPath :
            print(p, end='')
        print()
    inputNum = ReadInputNum()
    row = inputNum[0]
    column = inputNum[1]