class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        result = strs[0]
        for s in strs:
            common = ''
            for i in range(min(len(result), len(s))):
                if result[i] == s[i]:
                    common += s[i]
                else:
                    break
            result = common
        return result
        
