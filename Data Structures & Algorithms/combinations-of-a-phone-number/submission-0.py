class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits : return []
        res, cur = [], []
        digitsMap = {}
        digitsMap[2],digitsMap[3], digitsMap[4] = ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']
        digitsMap[5], digitsMap[6], digitsMap[7] = ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's']
        digitsMap[8], digitsMap[9] = ['t', 'u', 'v'], ['w', 'x', 'y', 'z']

        def backtrack(i):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            dig = int(digits[i])
            for c in digitsMap[dig]:
                cur.append(c)
                backtrack(i+1)
                cur.pop()
        backtrack(0)
        return res
        
