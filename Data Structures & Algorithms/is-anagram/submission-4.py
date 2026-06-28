class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # check the length of both strings
        # use a dictionary to store the differnt chars and the number of times they appear
        # need two for the two different strings
        # the key is the character, the value is the number of occurences
        # if the character is not in the dictionaty then insert and set its value to 1
        # if the character is already in the dictionary, the increment its value by 1
        # Finally, loop the dictionary: compare length, see if char is in the other, check the count
        
        if len(s) != len(t):
            return False

        first_anagram = dict()
        second_anagram = dict()

        # O(n)
        for char in s:
            
            if char not in first_anagram.keys():
                first_anagram[char] = 1
            else:
                first_anagram[char] += 1

        # O(n)
        for char in t:
            if char not in second_anagram.keys():
                second_anagram[char] = 1
            else:
                second_anagram[char] += 1

        if len(first_anagram) != len(second_anagram):
            return False

        for char in first_anagram.keys():
            if char not in second_anagram.keys():
                return False
            elif first_anagram[char] != second_anagram[char]:
                return False

        return True