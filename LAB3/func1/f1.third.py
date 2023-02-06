legs = 94 
heads = 35
def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if (2 * c + 4 * r) == numlegs:
            return (c, r)
    return "error data"
print(solve(heads , legs)) 
