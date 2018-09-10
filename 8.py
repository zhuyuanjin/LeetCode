class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        lst = str.split(' ')
        first = ''
        for i in lst:
            if i != '':
                first = i
                break
        cut = ''
        for i in first:
            if i not in '+-0123456789':
                break
            if cut != '' and (i not in '0123456789'):
                break
            cut += i
        try:
            return max(min(2**31-1, int(cut)), -2**31)
        except:
            return 0
