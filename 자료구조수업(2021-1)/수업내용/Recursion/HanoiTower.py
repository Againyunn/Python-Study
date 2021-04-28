def hanoiTower(n , source, dest, temp):
    if(n==1):
        print("Move a dist from %d to pegj %d  % (source, dest)")
        # print("Move a dist from peg {0} to peg {1}".format(source, dest))

    else:
        hanoiTower(n-1, source, temp, dest)
        print("Move a dist from %d to pegj %d  % (source, dest)")
        hanoiTower(n-1, temp, dest, source)
        # print("Move a dist from peg {0} to peg {1}".format(source, dest))