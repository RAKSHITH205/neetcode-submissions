class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis={"[":"]",
        "(":")",
        "{":"}"
        }
        stack=[]
        if s is None:
            return False
        for char in s:
            if char in paranthesis:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char!=paranthesis[stack.pop()]:
                    return False
        return not stack         
                

        

            


        