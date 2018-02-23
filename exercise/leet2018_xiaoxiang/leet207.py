class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}

        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        marked = set([])
        pathRecord = set([])
        for i in range(numCourses):
            res = self.dfsHelper(i, graph, marked, pathRecord)
            if not res:
                return False
        return True

    def dfsHelper(self, node, graph, marked, pathRecord):
        if node not in marked:
            marked.add(node)
            pathRecord.add(node)
            for adjNode in graph[node]:
                if adjNode in pathRecord:
                    return False
                res = self.dfsHelper(adjNode, graph, marked, pathRecord)
                if not res:
                    return False
            pathRecord.remove(node)
        return True
if __name__ == "__main__":
    s = Solution()
    numCourse = 7
    pairs = [[0, 1], [1, 2], [2, 3], [3, 5], [3, 4], [4, 2], [5, 4], [6, 4], [6, 5]]
    pairs = [[0, 1], [1, 2], [2, 3], [3, 5], [3, 4], [5, 4], [6, 4], [6, 5]]
    print(s.canFinish(numCourse, pairs))