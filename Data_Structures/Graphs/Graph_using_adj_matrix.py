'''Graph --  Graph is a network of nodes, where the data is stored in nodes and
nodes are interconnected by edges.
Undirected Graph -- There is no Direction for edges.
Adjacency matrix representation -- Graph is represented in matrix grid where each cell
contains either 1 or 0 which represents nodes are connected or not.'''

class Graph():
    #Time Comlexity -- O(n^2)
    def __init__(self,nodes,edges=[]):
        self.nodes = nodes
        self.num_of_nodes=len(nodes)
        self.matrix =[[0 for i in range(self.num_of_nodes)] for j in range(self.num_of_nodes)]
        self.edges=edges
        self.d=dict()
        self.dict=dict()
        for ind,node in enumerate(self.nodes):
            self.d[node]=ind
            self.dict[node]=list()
        self.build_graph()

    def build_graph(self):
        for i in range(self.num_of_nodes):
            self.matrix[i][i]= 1
        for (start,end) in self.edges :
            self.matrix[self.d[start]][self.d[end]]=1
            self.matrix[self.d[end]][self.d[start]]=1
            self.dict[start].append(end)
            self.dict[end].append(start)
            
    #Time Comlexity -- O(n^2)
    def add_edges(self,edges):
        for (start,end) in edges:
            self.matrix[self.d[start]][self.d[end]]=1
            self.matrix[self.d[end]][self.d[start]]=1
            self.dict[start].append(end)
            self.dict[end].append(start)

    #Time Comlexity -- O(n^2)
    def remove_edges(self,edges):
        for (start,end) in edges:
            self.matrix[self.d[start]][self.d[end]]=0
            self.matrix[self.d[end]][self.d[start]]=0
            self.dict[start].remove(end)
            self.dict[end].remove(start)

    #Time Comlexity -- O(n^2)
    def print_graph(self):
        print(" * ",end="")
        for node in self.nodes:
            print(f"{node}   ",end='')
        print()
        i=0
        for row in self.matrix:
            print(self.nodes[i],end=' ')
            print(row)
            i+=1
            


'''Weighted Grpah -- Additionally, each edge is associated with cost, which is called as weight. '''

class Weighted_graph():
    #Time Comlexity -- O(n^2)
    def __init__(self,nodes,edges=[]):
        self.nodes = nodes
        self.num_of_nodes=len(nodes)
        self.matrix =[[-1 for i in range(self.num_of_nodes)] for j in range(self.num_of_nodes)]
        self.edges=edges
        self.d=dict()
        self.dict=dict()
        for ind,node in enumerate(self.nodes):
            self.d[node]=ind
            self.dict[node]=list()
        self.build_graph()

    def build_graph(self):
        for i in range(self.num_of_nodes):
            self.matrix[i][i]= 0
        for (start,end,weight) in self.edges :
            self.matrix[self.d[start]][self.d[end]]=weight
            self.matrix[self.d[end]][self.d[start]]=weight
            self.dict[start].append(end)
            self.dict[end].append(start)

    #Time Comlexity -- O(n^2)
    def add_edges(self,edges):
        for (start,end,weight) in edges:
            self.matrix[self.d[start]][self.d[end]]=weight
            self.matrix[self.d[end]][self.d[start]]=weight
            self.dict[start].append(end)
            self.dict[end].append(start)

    #Time Comlexity -- O(n^2)
    def remove_edges(self,edges):
        for (start,end) in edges:
            self.matrix[self.d[start]][self.d[end]]=-1
            self.matrix[self.d[end]][self.d[start]]=-1
            self.dict[start].remove(end)
            self.dict[end].remove(start)

    #Time Comlexity -- O(n^2)
    def print_graph(self):
        print(" * ",end="")
        for node in self.nodes:
            print(f"{node}   ",end='')
        print()
        i=0
        for row in self.matrix:
            print(self.nodes[i],end=' ')
            print(row)
            i+=1
        
        
