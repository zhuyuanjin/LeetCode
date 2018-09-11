class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = ['(']
        while True:
            p = l.pop()
            if len(p) == 2 * n:
                l.append(p)
                break
            if p.count('(') > p.count(')'):
                l.insert(0, p+')')
            if p.count('(')<n:
                l.insert(0, p+'(')
        
        return l
