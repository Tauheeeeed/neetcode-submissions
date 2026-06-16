class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []
        if nums == 0:
            return false
        else:
            for value in nums:
                if value in new_list:
                    return True
                else:
                    new_list.append(value)
        return False
                
            
        
        