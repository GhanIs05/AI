from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        if self.graph:
            visited = [False] * (max(self.graph) + 1)
        else:
            print("Graph is empty.")
            return

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def addEdges(self):
        num_edges = int(input("Enter the number of edges: "))
        
        for _ in range(num_edges):
            u, v = map(int, input("Enter edge (u v): ").split())
            self.addEdge(u, v)

g = Graph()
g.addEdges()

start_vertex = int(input("Enter the starting vertex for BFS: "))
print("Following is Breadth First Traversal:")
g.BFS(start_vertex)
