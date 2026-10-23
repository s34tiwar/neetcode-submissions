from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        nodes_visited = 0
        while queue:
            node = queue.popleft()
            nodes_visited += 1

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        return nodes_visited == numCourses

             


        