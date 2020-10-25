# Lecandy problem Codechef (Array)

try:
    for _ in range(int(input())):
        number ,total_candies = map(int,input().split())
        candy_distribution = map(int,input().split())
        if total_candies < sum(candy_distribution):
            print("No")
        else:
            print("Yes")
except:
    pass



