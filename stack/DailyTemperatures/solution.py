def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)
    for idx in range(len(temperatures)):
        while stack and temperatures[idx] > temperatures[stack[-1]]:
            result[stack[-1]] = idx - stack[-1]
            print(f"DAY {idx} result is {result}")
            stack.pop()
        stack.append(idx)
        print(f"Now stack is: {stack} ")
    return result


temperatures = [30, 38, 30, 36, 35, 40, 28]
print(dailyTemperatures(temperatures))
