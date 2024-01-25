def solve(numheads, numlegs):
    for chickens in range(1, numheads):
        for rabbits in range(1, numheads):
            if chickens + rabbits == numheads and 4 * rabbits + 2 * chickens == numlegs:
                return chickens, rabbits
numheads, numlegs = 35, 94
x, y = solve(numheads, numlegs)
print(x, y)