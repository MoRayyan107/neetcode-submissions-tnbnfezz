class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            print(stack)
            
            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if not bool(stack): # !true if anything is present !false otherwise
                    return False

                rem = stack.pop()
                print(rem)
                if s[i] == ']' and rem != '[' or s[i] == '}' and rem != '{' or s[i] == ')' and rem != '(':
                    return False
        return not bool(stack)


