def min_adjacent_swaps(A, B):
    if sorted(A) != sorted(B):  
        return -1  

    n = len(A)
    A = list(A)  
    B = list(B)  
    swaps = 0  

    for i in range(n):
        if A[i] != B[i]:  
            j = i  
            while A[j] != B[i]:  
                j += 1  
            
            while j > i:  
                A[j], A[j - 1] = A[j - 1], A[j]
                j -= 1
                swaps += 1  

    return swaps

N = int(input())
A = input().strip()
B = input().strip()
print(min_adjacent_swaps(A, B))
