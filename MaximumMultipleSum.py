import math
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

def nC2(n):
    return (n * (n - 1)) // 2

def summing(n):
    return (n * (n + 1)) // 2

def fpow(n, p):
    if p == 0:
        return 1
    res = fpow(n, p >> 1)
    res *= res
    return res * n if p & 1 else res

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        ans = 2
        mulans = 2
        muls = 0
        
        for i in range(2, n + 1):
            muls = summing(n // i) * i
            
            if muls >= mulans:
                mulans = muls
                ans = i
                
        results.append(ans)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
