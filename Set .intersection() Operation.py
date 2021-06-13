#Set .intersection() Operation
#HackerRank Problem Solved

# Enter your code here. Read input from STDIN. Print output to STDOUT
num1=int(input())
set1=input().split()
set1=set(set1)
num2=int(input())
set2=input().split()
set2=set(set2)
intersection=set1.intersection(set2)
print(len(intersection))
