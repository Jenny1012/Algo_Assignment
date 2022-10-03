# 演算法分析機測
# 學號 : 10827201 | 10827243 | 10827245
# 姓名 : 簡湘媛     | 李筠婷   | 桑怡蓁
# 中原大學資訊工程系

# III. 霍夫曼碼 (Huffman Codes)

# A Huffman Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol # symbol name (character)
        self.left = left  # node left of current node
        self.right = right  # node right of current node
        self.huff = ''  # tree direction (0/1)
 
def getNodeHuff(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        getNodeHuff(node.left, newVal)
    if(node.right):
        getNodeHuff(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        i = chars.index(node.symbol)
        huffCode[i] = newVal
        '''
        for i in range(len(chars)):
            if chars[i] == node.symbol :
                huffCode[i] = newVal
                break
        '''
        #print(f"{node.symbol} -> {newVal}")
 
def decoding( encodeStr, node ) :
    root = node
    decodeStr = ''
    for c in encodeStr :
        if ( c == '0' ) :
            node = node.left
        elif (c == '1') :
            node = node.right

        if(not node.left and not node.right):
            decodeStr = decodeStr + node.symbol
            node = root
    return decodeStr


# characters for huffman tree
chars = []
 
# frequency of characters
freq = []

huffCode = [] 
# list containing unused nodes
nodes = []
codeNum = 0
#n = int( input("Please enter n : ") )
numCorrect = False
while not numCorrect :
    try :
        n = int( input("Please enter n : ") )
        if ( n < 0 ) :
            print("Please enter positive number.  Try again...")  
        else :
            numCorrect = True
    except ValueError :
        print("Please enter positive number.  Try again...")  


while n != 0 :
    codeNum = codeNum+1
    chars.clear()
    freq.clear()
    nodes.clear()
    huffCode.clear()
    huffCode = [''] * n
    for i in range(n) :
        #inputData = input().split()
        correct = False
        while not correct :
            inputData = input().split()
            if ( not inputData[0].isalpha() or not inputData[1].isdigit() or int(inputData[1]) <= 0 ) :
                print("error! Try again...")
            else :
                correct = True
        chars.append(inputData[0])
        freq.append(int(inputData[1]))
    
    binCorrect = False
    while not binCorrect :
        binCode = input("Please enter binary code : ")
        error = False
        for b in binCode :
            if b != '0' and b != '1' :
                error = True
                print("Bincode only contains [0,1]! Try again...")
                break
        if not error :
            binCorrect = True
    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        nodes.append(node(freq[x], chars[x]))
 
    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)
 
        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]
 
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
 
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
 
    # Huffman Tree is ready!
    getNodeHuff(nodes[0])
    decodeAns = decoding( binCode, nodes[0])

    print()
    print("Huffman Codes #", codeNum )
    for ch,huff in zip(chars, huffCode):
        print(ch, huff)
    
    print("Decode =", decodeAns)
    print()
    #n = int( input("Please enter n : ") )
    numCorrect = False
    while not numCorrect :
        try :
            n = int( input("Please enter n : ") )
            if ( n < 0 ) :
                print("Please enter positive number.  Try again...")  
            else :
                numCorrect = True
        except ValueError :
            print("Please enter positive number.  Try again...") 
