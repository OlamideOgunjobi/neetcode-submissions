class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # loop through each word in array
        # create a unique array for each word of length 26
        # initialize to all zeros and increment index to one when that letter exists (increment necessary for duplicate characters)
        # create a hashmap to group similar words, this array should be the key (convert the array to a tuple so it can be used as a key)
        # group words with similar arrays together
        # return the values of the dictionary but convert it to a list

        anagram_map = dict()

        for word in strs:
            arr = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                arr[index] += 1
            
            if tuple(arr) not in anagram_map:
                anagram_map[tuple(arr)] = [word]
            else:
                anagram_map[tuple(arr)].append(word)
            
        
        return list(anagram_map.values())
        
            