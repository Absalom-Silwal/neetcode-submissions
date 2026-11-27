class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        output = []
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [i]
            else:
                hash_map[nums[i]].append(i)
        
        for i in range(len(nums)):
            diff  = target - nums[i]
            if diff in hash_map:
                indexes = hash_map[diff]
                last_index = indexes.pop()
                if last_index == i:
                    continue
                else:
                    output =[i,last_index]
                    break

        return output


            
        