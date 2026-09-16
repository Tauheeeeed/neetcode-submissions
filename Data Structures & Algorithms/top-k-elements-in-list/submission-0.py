class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list={}
        for num in range(len(nums)):
            current_num = nums[num]
            if current_num in dict_list:
                dict_list[current_num] += 1
            else:
                dict_list[current_num] = 1
        sorted_list = dict(sorted(dict_list.items(),key = lambda item:item[1], reverse = True))
        most_freq = list(sorted_list.keys())
        return most_freq[:k]