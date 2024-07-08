def validPath(n: int, edges , source: int, destination: int) -> bool:
    paths = 0
    sec_item = None
    for i in edges:
        pickup = False
        if i[0] == source or sec_item == i[0]:
            pickup = True

        if pickup == True:
            sec_item = i[1]
            if sec_item == destination:
                paths += 1
                
        # print(paths)
        if paths == n :
            return True
    print(paths)
    return False

                
            




print(validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))