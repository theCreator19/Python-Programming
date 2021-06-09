#Nested Lists HackerRank Problem Solved
if __name__ == '__main__':
    a=[]
    nam=[]
    finalname=[]
    for _ in range(int(input())):
        name = input()
        
        score = float(input())
        nam.append(name)
        a.append(score)
    c=a
    #print(a)
    
    b=sorted(set(list(a)))[1]
    #print(b)
    for i in range(len(c)):
        if(c[i]==b):
            finalname.append(nam[i])
    
    finalsortednames=sorted(finalname)
    for i in range(len(finalsortednames)):
        print(finalsortednames[i])
