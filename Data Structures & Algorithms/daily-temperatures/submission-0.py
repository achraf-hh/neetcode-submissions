class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #list of pairs 
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                tempInd, tempAct = stack.pop()
                result[tempInd] = (i - tempInd)
            stack.append([i, t])
            

        return result
            



        