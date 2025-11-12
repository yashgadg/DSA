import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices                     
        self.graph = {v: [] for v in range(vertices)}  

    
    def add_edge(self, u, v, w):
       
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def display_adj_list(self, names):
        print("\nAdjacency List Representation:")
        for v in self.graph:
            print(f"{names[v]} -> ", end="")
            for (neighbor, weight) in self.graph[v]:
                print(f"{names[neighbor]}({weight}) ", end="")
            print()

    def display_adj_matrix(self, names):
        print("\nAdjacency Matrix Representation:")
        matrix = [[0]*self.V for _ in range(self.V)]
        for u in self.graph:
            for v, w in self.graph[u]:
                matrix[u][v] = w

        print("     " + "   ".join(names))
        for i in range(self.V):
            print(f"{names[i]:<5}", end=" ")
            for j in range(self.V):
                print(f"{matrix[i][j]:<3}", end=" ")
            print()

    def prim_mst(self, names):
        visited = [False] * self.V
        pq = []  
        result = [] 

        
        heapq.heappush(pq, (0, 0, -1))  
        total_weight = 0

        while pq:
            weight, u, parent = heapq.heappop(pq)

            if visited[u]:
                continue

            visited[u] = True
            total_weight += weight

            if parent != -1:
                result.append((parent, u, weight))

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(pq, (w, v, u))

        
        print("\nMinimum Spanning Tree (Using Prim's Algorithm):")
        for u, v, w in result:
            print(f"{names[u]} -- {names[v]}  (Distance: {w})")
        print("Total Distance of MST:", total_weight)



def main():
    
    names = ["Admin", "Computer", "Mechanical", "Civil", "Library"]
    g = Graph(len(names))

    
    g.add_edge(0, 1, 10) 
    g.add_edge(0, 2, 20)  
    g.add_edge(1, 2, 5)   
    g.add_edge(1, 3, 15)  
    g.add_edge(2, 3, 30) 
    g.add_edge(3, 4, 8)   
    g.add_edge(1, 4, 25) 

    g.display_adj_list(names)
    g.display_adj_matrix(names)
    g.prim_mst(names)


if __name__ == "__main__":
    main()

