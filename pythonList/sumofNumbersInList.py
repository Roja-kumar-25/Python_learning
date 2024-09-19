#to find the sum of numbers in the list
#approach 1
arr=list(map(int,input().split()))
n=len(arr)
res=(n*(n+1))//2
print(res)