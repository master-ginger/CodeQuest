#Given three numbers A, B, C. Print these numbers in ascending order followed by a 
#blank line and then the values in the sequence as they were read.

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