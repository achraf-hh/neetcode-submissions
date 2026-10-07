class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        for i, n in enumerate(arr):
            if len(arr[i:]) >= 2:
                res[i] = max(arr[i+1:])
            else : res[i] = -1
        return res 