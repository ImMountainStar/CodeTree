n = int(input())


def check(n):
    if (n%2 == 0) and ((n//10 + n%5) % 5 == 0):
       return('Yes')

    else : 
        return('No')

    



print(check(n))