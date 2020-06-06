class Interval:
    def __init__(self, st=None, ed=None):
        self.st = st
        self.ed = ed

    def merge(self, other):
        if other.st > self.ed: 
            if other.st - self.ed == 1:
                self.ed = max(other.ed, self.ed)
        elif other.ed < self.st:
            if self.st - other.ed == 1:
                self.st = min(other.st, self.st)
        else:
            self.st = min(self.st, other.st)
            self.ed = max(self.ed, other.ed)

    def length(self):
        return self.ed - self.st + 1

    def  __str__(self):
        return "[{}, {}]".format(self.st, self.ed)
    
    def __repr__(self):
        return self.__str__()

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st_dict = {}
        ed_dict = {}
        already_exists = set()
        for n in nums:
            if n in already_exists:
                continue
            already_exists.add(n)
            new_interval = Interval(n, n)
            print(new_interval)

            if n - 1 in ed_dict:
                prev_interval = ed_dict.pop(n - 1)
                new_interval.merge(prev_interval)

            if n + 1 in st_dict:
                next_interval = st_dict.pop(n + 1)
                new_interval.merge(next_interval)


            st_dict[new_interval.st] = new_interval
            ed_dict[new_interval.ed] = new_interval
            #print(st_dict)
            #print(ed_dict)
        return max(map(lambda r: r.length(), st_dict.values()))

if __name__ == "__main__":
    s = Solution()
    l = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(l))
