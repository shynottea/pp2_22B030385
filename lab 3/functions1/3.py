def solve(numheads, numlegs):
    chicks = numheads
    rabbs = 0
    while chicks != 35:
        if (chicks*2) + (rabbs*4) == numlegs:
            return chicks, rabbs
        chicks = chicks - 1
        rabbs = rabbs + 1