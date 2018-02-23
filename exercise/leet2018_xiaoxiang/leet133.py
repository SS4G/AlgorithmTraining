# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        marked = {}
        cloned = {}
        self.dfsGraph(node, marked, cloned)
        return cloned[node.label]

    def dfsGraph(self, node, marked, cloned):
        if node.label not in marked:
            marked.add(node.label)
            if node.label not in cloned:
                 cloned[node.label] = UndirectedGraphNode(node.label)
            for adj in node.neighors:
                if adj.label not in cloned:
                    cloned[adj.label] = UndirectedGraphNode(adj.label)
                cloned[node.label].neighbors.append(cloned[adj.label])
                self.dfsGraph(adj, marked, cloned)



