class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                result += dict[s[i]]
                continue
            if dict[s[i]]>=dict[s[i+1]]:
                result += dict[s[i]]
            else:
                result -= dict[s[i]]
                
        return result
