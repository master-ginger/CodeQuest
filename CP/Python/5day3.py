#https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Z

a,b,c,d=map(int,input().split())
if a**b > c**d:
    print("Yes")
else:
    print("No")

'''
sample input1:
3 2 5 4
output1:
No

sample input2:
5 2 4 2
output2:
Yes
'''