class Solution:

    def encode(self, strs: List[str]) -> str:

        

        result = ""

        for word in strs:
            result += str(len(word)) + "-" + word

        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        
        if len(s) == 0:
            return []
        # elif len(s) == 3:
        #     return [s[2]]

        result = []

        length = 0

        
        i = 0
        while i < len(s):
            new_word = ""

            # if s[i].isdigit() and s[i+1] == "-":
            if s[i] == 0:
                i += 2
                result.append("")
                continue

            length = s[i]
            while s[i+1].isdigit():
                i += 1
                length += s[i]

            length = int(length)
            
            i += 1
            if s[i] == "-":
                i += 1

            
            stopping_cond = i + length
            while i < stopping_cond:
                print(s[i])
                new_word += s[i]
                i += 1

            print(new_word)
            result.append(new_word)
            

        return result            
