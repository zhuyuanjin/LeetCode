class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = [[[i], [j for j in nums if j!=i]] for i in nums]
        while True:
            per, rest = lst.pop()
            if rest == []:
                lst.append([per, rest])
                break
            for i in rest:
                lst.insert(0, [per+[i], [j for j in rest if j!=i]])
        result = []
        for tup in lst:
            result.append(tup[0])
        return result
