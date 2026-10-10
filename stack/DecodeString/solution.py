def decodeString(s: str) -> str:
    current = ""
    stack_k = []
    stack_str = []
    k = 0
    for c in s:
        if c == "[":
            stack_k.append(k)
            stack_str.append(current)
            current = ""
            k = 0
        elif c.isdigit():
            k = k * 10 + int(c)
        elif c == "]":
            prev = stack_str.pop()
            num = stack_k.pop()
            current = prev + current * num
        else:
            current += c
    return current


s = "2[a3[b]]c"
print(decodeString(s))
