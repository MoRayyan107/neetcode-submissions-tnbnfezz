class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        S1count, S2count = [0]*26, [0]*26

        for i in range(len(s1)): 
            S1count[ord(s1[i]) - ord('a')] += 1
            S2count[ord(s2[i]) - ord('a')] += 1

        print("Current S1: ", S1count)
        print("Current S2: ", S2count)

        if S1count == S2count: 
            return True
        
        for right in range(len(s1), len(s2)):
            S2count[ord(s2[right]) - ord('a')] += 1
            S2count[ord(s2[right-len(s1)]) - ord('a')] -= 1
            print("S1: ", S1count)
            print("S2: ", S2count)
            if S1count == S2count:
                return True
        return False
        