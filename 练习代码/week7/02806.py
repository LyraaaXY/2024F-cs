while True:
    try:
        string_1, string_2 = input().split()
        dp = [[0]*len(string_2) for i in range(len(string_1))]
        
    except EOFError:
        break