class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        for i in s:
            if i in '([{':
                lst.append(i)
            else:
                if len(lst) == 0:
                    return False
                k = lst.pop()
                if k=='(':
                    if i == ')':
                        continue
                    else:
                        return False
                if k=='[':
                    if i == ']':
                        continue
                    else:
                        return False
                if k=='{':
                    if i == '}':
                        continue
                    else:
                        return False
        return len(lst) == 0
          
     
