'''BFS -- Breadth First Search -- Traverses a given graph level wise i.e by chosing a node as root.
Internally uses a Queue to store nodes to visit next.

DFS -- Depth First Search -- Traverses a given graph as deep as possible from a chosen node
before going to next node of same level.
Internally uses a Stack to store nodes to visit next.'''

from queue_using_linked_list import Queue #Refer Queue in Data Structures
from stack_using_linked_list import Stack #Refer Stack in Data Structures
from Graph import Graph #Refer Graph in Data Structures

def BFS(graph,root,visited,visit):
        visited[root] =1
        queue=Queue()
        queue.enqueue(root)
        visit.append(root)
        while queue.num_of_elements!=0:
            node=queue.dequeue()
            for adj in graph.dict[node]:
                if visited[adj] == 0:
                    visit.append(adj)
                    visited[adj] = 1
                    queue.enqueue(adj)

def DFS(graph,root,visited,visit):
        stack=Stack()
        stack.push(root)
        while stack.num_of_elements != 0:
            node = stack.pop()
            if visited[node] == 0:
                visit.append(node)
                visited[node] = 1
            for adj in reversed(graph.dict[node]):
                if visited[adj] == 0:
                    stack.push(adj)
    
class Graph_traversal_algo():
    def BFT(self,graph):
        visited = {}
        visit = []
        for node in graph.nodes:
            visited[node] = 0
        for node in visited :
            if visited[node] == 0:
                visit.append([])
                BFS(graph,node,visited,visit[-1])
        return visit

    def DFT(self,graph):
        visited = {}
        visit = []
        for node in graph.nodes:
            visited[node] = 0
        for node in visited :
            if visited[node] == 0:      
                visit.append([])
                DFS(graph,node,visited,visit[-1])
        return visit
