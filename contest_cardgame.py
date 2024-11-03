def solve(a1,a2,b1,b2):
    pairings = [
        [(a1, b1), (a2, b2)],
        [(a1, b2), (a2, b1)],
        [(a2, b1), (a1, b2)],
        [(a2, b2), (a1, b1)]
    ]
    
    suneet_wins = 0
    
    for pairing in pairings:
        sunnetwin = 0
        slavwin = 0
        
        for (a, b) in pairing:
            if a > b:
                sunnetwin += 1
            elif a < b:
                slavwin += 1
        
        if sunnetwin > slavwin:
            suneet_wins += 1
    
    return suneet_wins

games = int(input())

for _ in range(games):
    a1, a2, b1, b2 = map(int, input().split())
    res = solve(a1,a2,b1,b2)
    print(res)