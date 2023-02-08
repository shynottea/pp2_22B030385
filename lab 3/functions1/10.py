def unique(elements):
    x = []
    for i in range(len(elements)):
        if i not in x:
            x.append(i)
    return x