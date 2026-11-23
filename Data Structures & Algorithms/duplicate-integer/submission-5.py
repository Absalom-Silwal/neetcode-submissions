class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unq_num = set()
        # for num in nums:
        #     if num in unq_num:
        #         return True
        #     else:
        #         unq_num.add(num)
        # return False

        if len(nums) == len(set(nums)):
            return False
        return True                
        