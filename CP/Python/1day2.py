#https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/T

def sorted(brr):
    brr.sort()
    for i in range(3):
        print(brr[i])
    
arr=list(map(int,input().split()))
copy=arr.copy()
sorted(arr)
print("\b")
for i in range(3):
    print(copy[i])

'''
sample input1:
1 6 0
output1:
0
1
6

1
6
0

'''
