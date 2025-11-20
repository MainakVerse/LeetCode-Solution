'''
LOGIC: 
1. loop through the full list of strings (strs) 
2. check if character at index 0 of all words are same, then add that character to an empty string. 
3. keep checking for all the next characters till they are different for same index of each word.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: # no strings provided
            return "" # return empty string

        prefix = "" # set empty prefix sting
        first = strs[0] # get first word from the list of strings strs

        for i in range(len(first)): #get the characters from the first string one by one
            ch = first[i]

            for word in strs[1:]: # check in strings array
                if i >= len(word) or word[i] != ch: # if word is over or common substrings end
                    return prefix

            prefix += ch # keep adding the characters to prefix 

        return prefix
