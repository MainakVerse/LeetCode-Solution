'''Core logic: if a number added to left has lesser value than one in right, substract. Else add.
For eg: I = 1, V = 5. Hence, IV = 5-1 = 4 as I < V

Hence steps are:
1. Get a values dictionary with key of Roman literals and value of numbers.
2. The input is to be scanned against this dictionary and compared against values.
3. Follow the same logic and convert them from Roman to Integer keeping the add / subtract logic in mind

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0

        for i in range(len(s)-1):
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        total += values[s[-1]]

        return total

