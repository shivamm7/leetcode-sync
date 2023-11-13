class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_list = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels = []
        i = 0
        for c in s:
            if c in vowels_list:
                vowels.append(c)
            i += 1

        vowels.sort()

        result = ""
        i = 0
        for c in s:
            if c in vowels_list:
                result += vowels[i]
                i += 1
            else:
                result += c
        
        return result
        