while True:
    n = int(input())
    if n==0: 
        break
    
    Tian = sorted(list(map(int, input().split())))
    King = sorted(list(map(int, input().split())))
    
    lTian = 0; rTian = n - 1
    lKing = 0; rKing = n - 1
    ans = 0
    while lTian <= rTian:
        if Tian[lTian] > King[lKing]:
            ans += 1
            lTian += 1
            lKing += 1
        elif Tian[rTian] > King[rKing]:
            ans += 1
            rTian -= 1
            rKing -= 1
        else:
            if Tian[lTian] < King[rKing]:
                ans -= 1
            
            lTian += 1
            rKing -= 1
    
    print(ans*200)