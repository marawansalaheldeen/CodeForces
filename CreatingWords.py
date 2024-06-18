def main():
    
    n = int(input())
    
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    
    while(n):
        a,b = [str(i) for i in input().split()]
        arr1.append(a)
        arr2.append(b)
        
        temp = a[0]
        aS = list(a)
        aS[0] = b[0]
        k = ''.join(aS)
        
        bS = list(b)
        bS[0] = temp
        l = ''.join(bS)
        
        arr3.append(k)
        arr4.append(l)
        n = n - 1
        
    for i in range(len(arr1)):
        print(arr3[i],arr4[i])    

if __name__ == "__main__":
    main()