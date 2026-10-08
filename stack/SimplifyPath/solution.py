def simplifyPath(path: str) -> str:
    path = path.split("/")
    stack = []
    for p in path:
        if p == "" or p == ".":
            continue
        if p == "..":
            if stack:
                stack.pop()
            continue
        stack.append(p)
    return "/" + "/".join(stack)


path = "/neetcode/practice//...///../courses"

print(simplifyPath(path))
