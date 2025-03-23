from collections import deque

def min_of_max_brightness(k, brightness):
    n = len(brightness)
    dq = deque()
    max_values = []

    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and brightness[dq[-1]] <= brightness[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            max_values.append(brightness[dq[0]])

    return min(max_values)

k, n = map(int, input().split())
brightness = [int(input()) for _ in range(n)]
print(min_of_max_brightness(k, brightness))
