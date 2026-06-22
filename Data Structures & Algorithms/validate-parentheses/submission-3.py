class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for n in s:
            if n == "(" or n == "{" or n == "[":
                stack.append(n)
            else:
                if not stack :
                    return False
                x = stack.pop()
                if x == "(" and n ==")":
                    continue
                elif x =="{" and n =="}":
                    continue
                elif x =="[" and n =="]":
                    continue
                else:
                    return False 
        if stack:
            return False
        
        return True 