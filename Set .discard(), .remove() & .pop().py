# Set .discard(), .remove() & .pop()

# HackerRank Problem solved 

n = int(input())
s = set(map(int, input().split()))

m=int(input())
for i in range(m):
    a=input().split()
    if(a[0]=="pop"):
        s.pop()
    if(a[0]=="remove" ):
        s.remove(int(a[1]))
    if(a[0]=="discard"):
        s.discard(int(a[1]))
print(sum(s))
