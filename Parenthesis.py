class Solution:
    def isValid(self, s):
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        return not stack

print(Solution().isValid(s = "([]){}"))
