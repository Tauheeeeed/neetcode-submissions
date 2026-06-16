class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = []
        checked = [False] * len(strs)
        output = []
        for value in strs:
            counts = {}
            for char in value:
                if char in counts:
                    counts[char] += 1
                else: 
                    counts[char] = 1
            dict_list.append(counts)
        for i in range(len(dict_list)):
            if checked[i]:
                continue
            new_list = [strs[i]]
            checked[i] = True

            for j in range(i+1, len(dict_list)):
                if not checked[j] and dict_list[i] == dict_list[j]:
                    new_list.append(strs[j])
                    checked[j] = True
            output.append(new_list)
        return output      
            


                