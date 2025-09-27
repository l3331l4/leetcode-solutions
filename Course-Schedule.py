class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite = { course: [] for course in range(numCourses) }

        for course, prereq in prerequisites:
            prerequisite[course].append(prereq)

        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for prereq in prerequisite[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited.add(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        