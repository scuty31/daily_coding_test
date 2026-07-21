def solution(s):
    stack = []
    for i in range(len(s)):
        op = s[i]
        if op == '(':
            stack.append(op)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True