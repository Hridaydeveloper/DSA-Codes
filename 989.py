class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = 0
        result = []
        for i in range(len(num)):
            res = res * 10 + num[i]
        ans = res + k
        while ans > 0:
            digit = ans % 10
            result.append(digit)
            ans = ans // 10
        result.reverse()
        return result
        
        
