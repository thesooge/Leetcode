s = "({"

def isValid(s: str) -> bool:
    
    stack = []
    
    for i in s:
        if i in "({[":
            stack.append(i)
        
        elif not stack:
            return False

        elif i == ")":
            last = stack.pop()
            if last != "(":
                return False
            
        elif i == "}":
            last = stack.pop()
            if last != "{":
                return False

        elif i == "]":
            last = stack.pop()
            if last != "[":
                return False

    if stack:
        return False

    return True


    


print(isValid(s))