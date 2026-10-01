class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char in mapping:
                top_char = stack.pop() if stack else '#'

                if top_char != mapping[char]:
                    return False
                
            else:
                stack.append(char)
            

        return not stack



    




            