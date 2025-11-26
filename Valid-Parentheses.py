class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(','}':'{',']':'['}
        seen = []
        for char in s:
            if char in brackets:
                if seen and seen[-1] == brackets[char]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(char)
        return not seen
