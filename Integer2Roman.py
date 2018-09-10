class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lst = [0,0,0,0]
        i = 0
        while num > 0:
            lst[i] = num % 10
            num = int(num / 10)
            i += 1
        lst.reverse()
        result = ''
        result += 'M' * lst[0]
        if lst[1] == 9:
            result += 'CM'
        elif lst[1] == 5:
            result += 'D'
        elif lst[1] == 4:
            result += 'CD'
        elif lst[1] > 5 and lst[1]<9:
            result += 'D' + 'C'*(lst[1]-5)
        else:
            result += 'C'*lst[1]
            
        if lst[2] == 9:
            result += 'XC'
        elif lst[2] == 5:
            result += 'L'
        elif lst[2] == 4:
            result += 'XL'
        elif lst[2] > 5 and lst[2]<9:
            result += 'L' + 'X'*(lst[2]-5)
        else:
            result += 'X'*lst[2]
            
        if lst[3] == 9:
            result += 'IX'
        elif lst[3] == 5:
            result += 'V'
        elif lst[3] == 4:
            result += 'IV'
        elif lst[3] > 5 and lst[3]<9:
            result += 'V' + 'I'*(lst[3]-5)
        else:
            result += 'I'*lst[3]
        
        return result
