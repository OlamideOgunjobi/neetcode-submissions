class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        completed = [False] * len(strs)

        
        for i in range(len(strs)):
            if completed[i] == True:
                continue

            holder = [strs[i]]
            completed[i] = True

            for j in range(i+1, len(strs)):
                if not completed[j] and "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
                    holder.append(strs[j])  
                    completed[j] = True     
            result.append(holder)

        return result