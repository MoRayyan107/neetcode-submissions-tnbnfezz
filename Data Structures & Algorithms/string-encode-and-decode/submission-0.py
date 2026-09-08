class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedStr = ""
        for i in range(len(strs)):

            strLen = str(len(strs[i]))
            prefix = strLen+"#"
            encodedStr += prefix+strs[i]
        print(encodedStr)
        return encodedStr
            

    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        while ptr < len(s):

            i = ptr # holds the length in string format 
            while i < len(s) and s[i] != '#':
                i += 1
            # print(f"ptr: {ptr}")
            # print(f"how many numbers -> {i}")
            # print(s[ptr:i])

            strLen = int(s[ptr:i])
            # print(f"Length of string: {strLen}")
            ptr = i+1
            # print(f"ptr by 1 sinccce # {ptr}")

            res.append(s[ptr:strLen+ptr])
            # print(res)

            ptr += strLen
            # print(f"Updated PTR: {ptr}")
            # print("---------------------------------")

        return res



