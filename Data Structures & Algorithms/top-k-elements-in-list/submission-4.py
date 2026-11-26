class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        max_count = 0
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
            if hash_map[num] > max_count:
                max_count = hash_map[num]
        buckets = [[] for i in range(max_count)]
        for key in hash_map.keys():
            buckets[hash_map[key]-1].append(key)
        new_bucket = []
        for bucket in buckets:
            new_bucket += bucket
        
        return new_bucket[:-k-1:-1]

                

       
            



  
