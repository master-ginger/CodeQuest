#Given two numbers N and M. 
#Print the summation of their last digits.

a,b=map(int,input().split())
a1=a%10
b1=b%10
sum=a1+b1
print(sum)

'''
sample input:
567 863

output:
10
'''