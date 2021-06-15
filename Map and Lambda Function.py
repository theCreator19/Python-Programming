# Map and Lambda Function
# HackerRank problem solved using Python.

cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    c=[0,1]
    a,b=0,1
    if n==0:
        return []
    if(n==1):
        return [0]
    if(n==2):
        return [0,1]
    for i in range(n-2):
        
        if i%2==0:
            a=a+b
            c.append(a)
            
        else:
            b=a+b
            c.append(b)
    
    return c

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
