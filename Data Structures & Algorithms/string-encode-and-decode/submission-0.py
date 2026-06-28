class Solution:

    def __init__(self):
        self.word_length = []

    def encode(self, strs: List[str]) -> str:
        my_new_word = ""
        for word in strs:
            self.word_length.append(len(word))   # save the length of the word
            for c in word:
                my_new_word += chr(ord(c) + 1)  # encode each letter
        return my_new_word

    def decode(self, s: str) -> List[str]:
        decode_array = ["" for i in range(len(self.word_length))]
        for i, length in enumerate(self.word_length):
            for c in s[0:length]:
                decode_array[i] += chr(ord(c) - 1)  # decoding each letter

            s = s[length:]
        
        return decode_array