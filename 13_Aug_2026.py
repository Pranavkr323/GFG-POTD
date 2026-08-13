# GFG POTD - 2026-08-13
# Longest Path in a Directed Acyclic Graph
# Kahn's Algorithm (Topological Sort) + Dynamic Programming

from collections import deque
class Solution:
    def maxDistance(self, V, src, edges):
        INT_MIN = -2**31
        # code here
        queue = deque()
        indegree = [0] * V
        dist = [INT_MIN] * V
        dist[src] = 0
        order = []
        graph = [[] for _ in range(V)]

        for u,v,w in edges:
            graph[u].append([v,w])
            indegree[v] += 1
            
        for verti in range(V):
            if indegree[verti] == 0:
                queue.append(verti)
                
        while queue:
            processed = queue.popleft()
            order.append(processed)
            
            for v, w in graph[processed]:
                indegree[v] -= 1
                
                if indegree[v] == 0:
                    queue.append(v)
                    
        for u in order:
            for v, w in graph[u]:
                if dist[u] != INT_MIN:
                    dist[v] = max(dist[v], dist[u] + w)
                
        return dist
            
    
