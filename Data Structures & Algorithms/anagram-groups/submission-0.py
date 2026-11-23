class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for strin in strs:
            sort_str = "".join(sorted(strin))
            if sort_str not in hash_map:
                hash_map[sort_str] = [strin]
            else:
                hash_map[sort_str].append(strin)
        
        return list(hash_map.values())
        