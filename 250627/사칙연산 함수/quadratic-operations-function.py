a, o, c = input().split()
a = int(a)
c = int(c)


def plus(a,c):
    answer = a + c 
    return (print(f'{a} {o} {c} = {answer}'))

def minus(a,c):
    answer = a - c 
    return (print(f'{a} {o} {c} = {answer}')) 

def divede(a,c):
    answer = a // c 
    return (print(f'{a} {o} {c} = {answer}')) 

def triple(a,c):
    answer = a * c 
    return (print(f'{a} {o} {c} = {answer}')) 

if o == '+':
    (plus(a,c))

elif o == '-':
    (minus(a,c))

elif o == '/':
    (divede(a,c))

elif o == '*':
    (triple(a,c))


else:
    print('False')
# Please write your code here.