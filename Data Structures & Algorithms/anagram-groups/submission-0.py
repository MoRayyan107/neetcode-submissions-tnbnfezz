class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hash_map = {}

        for Str in strs:
            freqArray = [0]*26
            
            for char in Str:
                freqArray[ord(char) - ord('a')] += 1

            key = tuple(freqArray)

            if key in hash_map:
                hash_map[key].append(Str)
            else:
                hash_map[key] = [Str]
            
        print(hash_map.values())
        

        return list(hash_map.values())
    