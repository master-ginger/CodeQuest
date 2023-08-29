#https://codeforces.com/group/MWSDmqGsZm/contest/326907/problem/D

t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    sum=0
    for i in range(l,r+1):
        sum+=i
    print(sum)

'''
sample input:
4
3 6
2 11
4 16
7 17

output:
18
65
130
132
'''