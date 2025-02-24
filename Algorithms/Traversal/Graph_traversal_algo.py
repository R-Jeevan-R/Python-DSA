'''BFS -- Breadth First Search -- Traverses a given graph level wise i.e by chosing a node as root.
Internally uses a Queue to store nodes to visit next.

DFS -- Depth First Search -- Traverses a given graph as deep as possible from a chosen node
before going to next node of same level.
Internally uses a Stack to store nodes to visit next.'''

from queue_using_linked_list import Queue #Refer Queue in Data Structures
from stack_using_linked_list import Stack #Refer Stack in Data Structures
from Graphs_using_adj_matrix import Graph #Refer Graph in Data Structures
class Graph_traversal_algo():
    #Time Complexity -- O(V+E), where V - Number of nodes/vertices and E - Number of edges
    def BFS(self,graph,root):
        visited=set()
        visited.add(root)
        queue=Queue()
        queue.enqueue(root)
        print(f'{root}-->',end=' ')
        while queue.num_of_elements!=0:
            node=queue.dequeue()
            for adj in graph.dict[node]:
                if adj not in visited:
                    print(f'{adj}-->',end=' ')
                    visited.add(adj)
                    queue.enqueue(adj)

    #Time Complexity -- O(V+E), where V - Number of nodes/vertices and E - Number of edges                  
    def DFS(self,graph,root):
        visited=set()
        visited.add(root)
        stack=Stack()
        stack.push(root)
        print(f'{root}-->',end=' ')
        while stack.num_of_elements != 0:
            node = stack.pop()
            if node not in visited:
                print(f'{node} -->', end=' ')
                visited.add(node)
            for adj in reversed(graph.dict[node]):
                if adj not in visited:
                    stack.push(adj)
