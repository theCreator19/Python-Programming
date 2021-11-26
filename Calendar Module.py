# Calendar Module


# HackerRank Problem Solved using Python


# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
a=map(int,input().split())
a=list(a)
b=calendar.weekday(a[2],a[0],a[1])
if(b==5):
    c="SATURDAY"
if(b==6):
    c="SUNDAY"
if(b==0):
    c="MONDAY"
if(b==1):
    c="TUESDAY"
if(b==2):
    c="WEDNESDAY"
if(b==3):
    c="THURSDAY"
if(b==4):
    c="FRIDAY"
print(c)
