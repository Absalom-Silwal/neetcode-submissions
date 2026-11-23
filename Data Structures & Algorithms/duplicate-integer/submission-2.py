class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unq_num = []
        # for num in nums:
        #     if num in unq_num:
        #         return True
        #     else:
        #         unq_num.append(num)

        # return False
        if sorted(nums) == sorted(list(set(nums))):
            return False
        return True                
        