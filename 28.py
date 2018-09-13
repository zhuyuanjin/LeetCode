class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        nn = len(needle)
        while i < len(haystack)-len(needle)+1:
            j = 0
            result = True
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    result = False
                    break
                j+=1
            if result:
                return i
            i+=1
        return -1
