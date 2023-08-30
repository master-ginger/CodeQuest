#https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y

a,b,c,d=map(int,input().split())
mul=a*b*c*d
print(mul%100)

'''
sample input1:
5 7 2 4
output1:
80

sample input2:
3 9 9 9
output2:
87
'''