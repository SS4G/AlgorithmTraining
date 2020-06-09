from collections import namedtuple
class Solution(object):
    def getRoot(self, n, prevMap):
        while prevMap[n] != n:
            n = prevMap[n]
        return n

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        Equation = namedtuple("Equation", ["n1", "n2", "cond"])
        eqs = []
        allNodes = set()
        for eq in equations:
            n1 = eq[0]
            n2 = eq[3]
            allNodes.add(n1)
            allNodes.add(n2)
            cond = eq[1:3] == "=="
            eqs.append(Equation(n1=n1, n2=n2, cond=cond))
        
        prevMap = {n:n for n in allNodes}
        print(eqs)
        for eq in eqs:
            if eq.n1 == eq.n2 and not eq.cond:
                return False
            #print("jj", eq.n)
            if eq.n1 != eq.n2 and eq.cond:
                print("hh")
                n1root = self.getRoot(eq.n1, prevMap)
                n2root = self.getRoot(eq.n2, prevMap)
                 
                prevMap[n2root] = n1root
        print(prevMap)
        for eq in eqs:
            if not eq.cond:
                n1root= self.getRoot(eq.n1, prevMap)
                n2root = self.getRoot(eq.n2, prevMap)
                if n1root == n2root:
                    return False
        return True

if __name__ == "__main__":
    case1 = ["a==b","b==c","a==c"]
    case2 = ["a==b","b!=c","c==a"]
    case3 = ["c==c","b==d","x!=z"]
    case4 = ["a==b","b!=a"]
    s = Solution()
    #assert s.equationsPossible(case1)
    #assert not s.equationsPossible(case2)
    #assert s.equationsPossible(case3)
    assert not s.equationsPossible(case4)

