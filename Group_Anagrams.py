class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            if ''.join(sorted(i)) in dic:
                dic[''.join(sorted(i))].append(i)
            else:
                dic[''.join(sorted(i))] = [i]
        return list(dic.values())
