class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        # for strin in strs:
        #     sort_str = "".join(sorted(strin))
        #     if sort_str not in hash_map:
        #         hash_map[sort_str] = [strin]
        #     else:
        #         hash_map[sort_str].append(strin)
        
        # return list(hash_map.values())

        for word in strs:
            freq_count = [0]*26
            for char in word:
                freq_count[ord(char)-ord('a')] += 1

            #hash_key = str(freq_count)
            hash_key = "$".join([str(x) for x in freq_count ])


            if hash_key not in hash_map:
                hash_map[hash_key]=[word]
            else:
                hash_map[hash_key].append(word)
        return list(hash_map.values())
            
        