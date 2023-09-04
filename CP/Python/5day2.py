#https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/U

a=float(input())

b=int(a)
if a==b:
    print("Integer",b)
else:
    print("Float",b,"{:.3f}".format(a-b))

'''
sample input1:
234.000
output1:
Integer 234

sample input2:
5334.578
output2:
Float 5334 0.578
'''