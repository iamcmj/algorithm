def cantor(N):
    space = " "
    if N == 0:
        return "-"
    elif N == 1:
        return "-" + space + "-"
    else:
        return cantor(N - 1) + space * (3 ** (N - 1)) + cantor(N - 1)


while True:
    try:    
        N = int(input())
        print(cantor(N))
    except:
        break