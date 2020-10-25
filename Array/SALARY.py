try:
    for _ in range(int(input())):
        # n = number of workers
        n = int(input())
        arr = list(map(int,input().split()))
        minimum = min(arr)
        sum_arr = sum(arr)
        moves = sum_arr - (n * minimum)
        print(moves)
except:
    pass