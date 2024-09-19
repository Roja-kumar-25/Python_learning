#to findout the unique numbers in the given list
# approach1
arr=list(map(int,input().split()))
l1=[]
for i in range(len(arr)):
    if arr[i] not in l1:
        l1.append(arr[i])
    else:
        pass
print(l1)