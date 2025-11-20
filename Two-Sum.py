# Create a hashmap that saves both value and index.
# Iterate through array and check if the index equals complement. 
# In 1st case it will always be false as hashmap is empty, so add the first occurence to hashmap.
# If the 2nd occurence, the element may or may not be equal to complement. If not add it to the hashmap.
# If match, then return the present index of the element and also the index of the complement that adds up together to the target.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # define a hashmap to save the numbers and indices
        for i, x in enumerate(nums): # enumerate automatically assigns index to a value
            comp = target - x # comp or complement is the value which is to be found in the code. x is the one found by iteration
            if comp in seen: 
                return [i, seen[comp]] # if complement is in hashmap, then return its index and the present element's index in the array. When saving the x via iteration its index was already saved in hashmap
            seen[x] = i # if the value of x is not matching the complement value, add it with its index to the hashmap.

        return []
