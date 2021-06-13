# Symmetric Difference
# HackerRank Problem Solved using Python
# Enter your code here. Read input from STDIN. Print output to STDOUT
num1=int(input())
set1=input().split()
set1=set(set1)
num2=int(input())
set2=input().split()
set2=set(set2)
sd=set1.symmetric_difference(set2)
sd=list(sd)
for i in range(len(sd)):
    sd[i]=int(sd[i])
sd=sorted(sd)
for i in range(len(sd)):
    print(sd[i])
