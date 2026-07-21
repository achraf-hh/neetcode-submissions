class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        l, r = 0, len(s1)
        letters = {}
        current_window = {}
        for s in s1:
            if s in letters:
                letters[s] += 1
            else:
                letters[s] = 1
        for i in range(l, r):
            if s2[i] in current_window :
                current_window[s2[i]] += 1
            else:
                current_window[s2[i]] = 1
        if current_window == letters :
            return True
        while r < len(s2):
            if s2[r] in current_window:
                current_window[s2[r]] +=1
            else:
                current_window[s2[r]] = 1
            current_window[s2[l]] -= 1
            if current_window[s2[l]] <= 0:
                current_window.pop(s2[l])
            if current_window == letters :
                return True
            l += 1
            r += 1
        return False



        