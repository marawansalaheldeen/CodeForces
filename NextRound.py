n,k = [int(i) for i in input().split()]
ari = input().split()
arr = [int(i) for i in ari]
k = k-1
count = 0 
kth = arr[k]

arr.sort()
arr.reverse()

for i in range(len(arr)):
    if arr[i] > kth or (arr[i] == kth and arr[i]!=0) :
        
        count = count + 1   
        
        
print(count)

