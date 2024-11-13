from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')

                for neighbour in reversed(self.graph[vertex]):
                    if neighbour not in visited:
                        stack.append(neighbour)

g = Graph()

num_edges = int(input("Enter the number of edges: "))
print("Enter the edges in the format 'u v':")
for _ in range(num_edges):
    u, v = map(int, input().split())
    g.addEdge(u, v)

start_vertex = int(input("Enter the starting vertex for DFS: "))

print(f"Following is DFS starting from vertex {start_vertex}")
g.DFS(start_vertex)
