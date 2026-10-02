def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for asteroid in asteroids:
        if not stack:
            stack.append(asteroid)
        elif stack[-1] > 0 and asteroid < 0:
            if abs(stack[-1]) > abs(asteroid):
                continue
            elif abs(stack[-1]) == abs(asteroid):
                stack.pop()
                continue
            else:
                while stack and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                if not stack:
                    stack.append(asteroid)
        else:
            stack.append(asteroid)
    return stack


def asteroidCollision2(asteroids: list[int]) -> list[int]:
    stack = []
    for asteroid in asteroids:
        alive = True
        while stack and stack[-1] > 0 and asteroid < 0:
            if abs(stack[-1]) < abs(asteroid):
                stack.pop()
            elif abs(stack[-1]) == abs(asteroid):
                stack.pop()
                alive = False
                break
            else:
                alive = False
                break
        if alive:
            stack.append(asteroid)
    return stack


asteroids = [2, 4, -4, -1]

print(asteroidCollision(asteroids))
