def evalRPN(tokens: list[str]) -> int:
    stack = []
    for t in range(len(tokens)):
        if tokens[t] == "+":
            first = stack.pop()
            second = stack.pop()
            stack.append(first + second)
        elif tokens[t] == "-":
            first = stack.pop()
            second = stack.pop()
            stack.append(second - first)
        elif tokens[t] == "*":
            first = stack.pop()
            second = stack.pop()
            stack.append(first * second)
        elif tokens[t] == "/":
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second / first))
        else:
            stack.append(int(tokens[t]))

    return stack[0]


tokens = ["1", "2", "+", "3", "*", "4", "-"]

print(evalRPN(tokens))
