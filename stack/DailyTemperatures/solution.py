def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)
    for idx in range(len(temperatures)):
        while stack and temperatures[idx] > temperatures[stack[-1]]:
            result[stack[-1]] = idx - stack[-1]
            stack.pop()
        stack.append(idx)
    return result


temperatures = [30, 38, 30, 36, 35, 40, 28]
print(dailyTemperatures(temperatures))
