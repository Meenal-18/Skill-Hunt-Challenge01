def preprocess_treasures(s):
    n = len(s)
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if s[i] == 'T' else 0)

    return prefix

def count_treasures(prefix, start, end):
    return prefix[end] - prefix[start - 1]

s = input().strip()
n = int(input())

prefix = preprocess_treasures(s)

for _ in range(n):
    start, end = map(int, input().split())
    print(count_treasures(prefix, start, end))
