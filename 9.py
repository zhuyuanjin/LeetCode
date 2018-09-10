class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)
        result = True
        for i in range(int(n/2)):
            if x[i] != x[n-1-i]:
                result = False
        return result
  
