
class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def BFS(self, vertex):
        visited = [vertex]
        queue = [vertex]
        self.pd = {}
        while queue:
            deVertex = queue.pop(0)
            #print('deVertex=',deVertex)
            for adjecent in self.gdict[deVertex]:
                if adjecent not in visited:
                    #print(adjecent)
                    visited.append(adjecent)
                    queue.append(adjecent)
                    self.pd[adjecent] = deVertex
        #print(self.pd) 
    
    def SSSP(self,start, end):
        self.BFS(start)
        l=[]
        x=end
        while(x!=start):
            l.append(x)
            x=self.pd[x]
        l.append(x)
        print(l)
    
    
customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"],
               "f" : ["e", "d", "g"]
            }
        
g = Graph(customDict)

#g.BFS('a')
#print(g.pd)
g.SSSP("a","e")
