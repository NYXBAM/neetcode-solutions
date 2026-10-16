def make_guess(pick):
    def guess(num):
        if num == pick:
            return 0
        elif num > pick:
            return -1
        else:
            return 1

    return guess


def guessNumber(n: int, pick) -> int:
    left = 1
    right = n
    guess = make_guess(pick)
    while left <= right:
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            right = mid - 1
        else:
            left = mid + 1
    return -1


n = 15
pick = 10

print(guessNumber(n, pick))
