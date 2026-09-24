def isValid(s: str) -> bool:
    stack = []

    for n in s:
        if n == "{" or n == "[" or n == "(":
            stack.append(n)
        else:
            if not stack:
                return False
            if n == ")" and stack[-1] == "(":
                stack.pop()
            elif n == "]" and stack[-1] == "[":
                stack.pop()
            elif n == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

    return not stack


s = "([{}])"
print(isValid(s))
