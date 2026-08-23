s = "node"
t = "neetcode"


def isSubsequence(s: str, t: str) -> bool:
    s_pntr = 0
    t_pntr = 0
    while s_pntr < len(s) and t_pntr < len(t):
        if s[s_pntr] == t[t_pntr]:
            s_pntr += 1
        t_pntr += 1

    return s_pntr == len(s)


print(isSubsequence(s, t))
