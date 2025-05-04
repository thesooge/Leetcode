def numEquivDominoPair(dominoes):
    hshmap = {}
    for domino in dominoes:
        hshmap[tuple(sorted(domino))] = hshmap.get(tuple(sorted(domino)), 0) + 1
    
    total = 0
    for value in hshmap.values():
        if value > 1:
            total += value * (value - 1) // 2

    return total

    

dominoes = [[1,2],[2,1],[3,4],[5,6]]

print(numEquivDominoPair(dominoes))