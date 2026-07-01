class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        map1, map2 = [0] * 26, [0] * 26

        # O(a) where a is the length of s1
        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1
        

        matches = 0
        for i in range(26):
            if map1[i] == map2[i]:
                matches += 1

        i = 0
        for j in range(len(s1), len(s2)): # start from where we stopped till the end of s2
            if matches == 26:   # if they are exactly the same, return true
                return True

            index = ord(s2[j]) - ord('a')
            map2[index] += 1

            if map2[index] == map1[index]:  # if the update made them equal
                matches += 1
            elif map2[index] == map1[index] + 1:    # if the update made them unequal
                matches -= 1

            index = ord(s2[i]) - ord('a')
            map2[index] -= 1
            if map2[index] == map1[index]:  # if the update made them equal
                matches += 1
            elif map2[index] == map1[index] - 1:    # if the update made them unequal
                matches -= 1

            i += 1

        return matches == 26