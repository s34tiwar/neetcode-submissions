from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        # make a directed graph 
        # [course, prereq]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        queue = deque()
        
        # course that we can take immediatelu 
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []
        # do bfs 
        while queue:
            course = queue.popleft()
            order.append(course)

            for next_courses in adj[course]:
                indegree[next_courses] -= 1
                if indegree[next_courses] == 0:
                    queue.append(next_courses)
        # if some courses never got processed, there is a cycle 
        if len(order) != numCourses:
            return []
        else:
            return order

