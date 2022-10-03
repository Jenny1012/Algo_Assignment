INFINITY = 1e30
WHITE = 1
GRAY = 2
BLACK = 3

class AdjacencyMatrix:
	def __init__ ( self, n_vertices ):
		self.n_vertices = n_vertices
		self.n_edges = 0
		self.A = [ [ 0 for j in range( n_vertices + 1 )] for i in range( n_vertices + 1 ) ]

		self.color = [ 0 for i in range( n_vertices + 1 ) ]
		self.d     = [ 0 for i in range( n_vertices + 1 ) ]
		self.pi    = [ 0 for i in range( n_vertices + 1 ) ]
		self.f     = [ 0 for i in range( n_vertices + 1 ) ]

		self.time = 0
		self.TS_list = []

	def SetDirectedEdgeWeight( self, start_vertex, end_vertex, weight ):
		if ( start_vertex >= 1 and start_vertex <= self.n_vertices and 
			 end_vertex >= 1 and end_vertex <= self.n_vertices ):
			if ( self.A[start_vertex][end_vertex] == 0 ):
				self.A[start_vertex][end_vertex] = weight
				self.n_edges += 1

	def Dijkstra( self, source ):
		# Initialization
		for i in range( 1, self.n_vertices + 1 ):
			self.d[i] = INFINITY
		self.d[source] = 0
		self.pi[source] = 0

		set = [True] * ( self.n_vertices + 1 )

		n = self.n_vertices
		while ( n != 0 ):
			# Extract Minimum
			u = 0
			min = INFINITY
			for i in range( 1, self.n_vertices + 1 ):
				if ( set[i] and self.d[i] < min ):
					u = i
					min = self.d[i]
			set[u] = False
			n -= 1

			# Relax
			for v in range( 1, self.n_vertices + 1 ):
				if ( self.A[u][v] != 0 ):
					if ( self.d[v] > self.d[u] + self.A[u][v] ):
						self.d[v] = self.d[u] + self.A[u][v]
						self.pi[v] = u

def ReadInputNum() :
    global inputNum
    try :
        inputNum = list( map( int, input("Please enter the num of node and edge: ").split() ) )
        if ( inputNum[0] < 0 or  inputNum[1] < 0 ) :
            print( "Please enter range in [1,100].  Try again...")
            ReadInputNum()

    except ValueError :
        print("That was no valid number.  Try again...")    
        print()
        ReadInputNum()
    return inputNum
    
def ReadInputNode() :
    global inputnode
    inputstr = input( "please enter the name of node :  " )
    inputnode = inputstr.split()
    if ( inputstr.islower() == False ):
        print( "Nodes must be lowercase.  Try again...")
        ReadInputNode()
    elif ( inputnode[0] != 's' ) :
        print( "First node must be s.  Try again...")
        ReadInputNode()
    return inputnode

def ReadWeight( nodelist ) :
    global inputweight
    
    try :
        inputweight = input( "please enter the start node, end node and weight :  " ).split()
        if ( len(inputweight) != 3 ) :
            ReadWeight(  nodelist )
        elif ( inputweight[0].islower() == False or inputweight[1].islower() == False ):
            print( "Node must be lowercase.  Try again...")
            ReadWeight( nodelist )
        elif ( inputweight[2].isdigit == False ) :
            print( "Weight must be number .  Try again...")
            ReadWeight( nodelist )
            
        nodelist.index(inputweight[0])
        nodelist.index(inputweight[1])

    except ValueError :
        print('node is not in list')
        ReadWeight( nodelist )
        
    return inputweight

 
inputNum = ReadInputNum()
numOfnode = inputNum[0]
numOfedge = inputNum[1]
g = 1 

while ( numOfnode != 0 and numOfedge != 0 ) :
    G = AdjacencyMatrix( numOfnode )
    nodelist = ReadInputNode() 

    for i in range ( numOfedge ) :
        setlist = ReadWeight(nodelist)
        G.SetDirectedEdgeWeight( nodelist.index(setlist[0])+1, nodelist.index(setlist[1])+1, int(setlist[2]) )

    G.Dijkstra( 1 )
    print()
    print ( "Graph #%d" %g )
    for i in range( 2, G.n_vertices + 1 ):
        print ( "From s to", nodelist[i-1], "=", G.d[i] )
     
    print( "\ns source node" )
    for i in range( 2, G.n_vertices + 1 ):
        print( nodelist[i-1]+"'s parent node =", nodelist[ G.pi[i]-1] )
        #print( "Vertex", nodelist[i-1], "Distance to souce =", G.d[i], "Parent =", nodelist[ G.pi[i]-1] )
    
    inputNum = ReadInputNum()
    numOfnode = inputNum[0]
    numOfedge = inputNum[1]
    g = g + 1 
