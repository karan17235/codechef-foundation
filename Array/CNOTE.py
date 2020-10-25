# Chef and notebooks problem Codechef

try:
    for _ in range(int(input())):
        # x = total number of pages the chef has to write
        # y = number of pages left in his current notebook
        # k = amount of money left with chef
        # n = number of notebooks showed by the shopkeeper
        x, y, k , n = map(int, input().split())
        # p = number of pages in the new notebook
        # c = the cost of new notebook
        output = []
        for _ in range(n):
            p , c = map(int, input().split())
            if ((y+p) >= x) and k >= c:
                output.append("LuckyChef")
            else:
                output.append("UnluckyChef")
        if "LuckyChef" in output:
            print("LuckyChef")
        else:
            print("UnluckyChef")
except: 
    pass