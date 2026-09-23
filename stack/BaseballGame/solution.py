def calPoints(operations: list[str]) -> int:
    records = []
    for op in operations:
        if op == "+":
            records.append(records[-2] + records[-1])
        elif op == "D":
            records.append(records[-1] * 2)
        elif op == "C":
            records.pop()
        else:
            records.append(int(op))

    return sum(records)


ops = ["1", "2", "+", "C", "5", "D"]

print(calPoints(ops))
