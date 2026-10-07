def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = list(zip(position, speed))
    cars.sort(reverse=True)
    last_time = 0
    fleet = 0
    for car in cars:
        time = (target - car[0]) / car[1]
        if time > last_time:
            fleet += 1
            last_time = time
    return fleet


target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

print(carFleet(target, position, speed))
