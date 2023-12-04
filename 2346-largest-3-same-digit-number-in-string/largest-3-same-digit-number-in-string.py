class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        n = len(num)
        ans = ""
        while i < n:
            if i + 1 < n and num[i] == num[i+1]:
                i += 1
                if i + 1 < n and num[i] == num[i+1]:
                    if ans == "" or ans < num[i]:
                        ans = num[i]
            i += 1
        
        return ans * 3