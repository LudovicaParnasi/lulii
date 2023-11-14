class DGraph:
    def __init__(self):
        self.edges = {}
        
    def newNode(self, n):
        '''creates a node with label 'n' in the graph'''
        if n in self.edges:
            raise ValueError('node already present')
        self.edges[n] = []
        
    def newEdge(self, s, d):
        if s not in self.edges and d not in self.edges: #check if source and destinations are nodes of the graph
            raise ValueError('nodes not present, creates them before cretaing an edge between them')
        else:
            self.edges[s].append(d)
        
    def getNodes(self):
        listnodes = []
        for i in self.edges:
            listnodes.append(i)
        return listnodes
    
    
    def getOut(self, n):
        if n in self.edges: 
            return self.edges[n]
                




#print(allIn('d',g))

#print(g.getOut('a'))
#print(g.getNodes())

