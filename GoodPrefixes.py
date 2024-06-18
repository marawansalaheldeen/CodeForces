def count_good_prefixes(t, test_cases):
    results = []
 
    for case in test_cases:
        n, a = case
        total_sum = 0
        max_element = 0
        good_count = 0
 
        for i in range(n):
            total_sum += a[i]
            max_element = max(max_element, a[i])
            if total_sum - max_element == max_element:
                good_count += 1
 
        results.append(good_count)
 
    return results
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
 
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        test_cases.append((n, a))
 
    results = count_good_prefixes(t, test_cases)
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()