# Last updated: 20/05/2025, 20:37:22
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        seen=[False]*n
        def dfs(current_node):
            if current_node ==destination:
                return True
            seen[current_node]=True
            for edge in graph[current_node]:
                if not seen[edge]:
                    if dfs(edge):
                        return True
            return False

        return dfs(source)        