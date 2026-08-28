def encode(strs: list[str]) -> str:
    delimiter = "#"
    result = []
    for s in strs:
        result.append(str(len(s)) + delimiter + s)
    return "".join(result)


string = ["Hello", "World"]
print(encode(string))


def decode(st: str) -> list[str]:
    i = 0
    res = []
    while i < len(st):
        j = st.find("#", i)
        length = int(st[i:j])
        res.append(st[j + 1 : j + 1 + length])
        i = j + 1 + length

    return res


print(decode("5#Hello5#World"))
