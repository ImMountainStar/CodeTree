a, b = map(int, input().split())

def mlutilple(a,b):
    answer = 1 
    while b>0:
        answer = answer*a 
        b = b-1 

    return answer 


print(mlutilple(a, b))
# Please write your code here.