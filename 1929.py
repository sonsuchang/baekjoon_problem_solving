import sys
M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if i == 1:
        continue
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            break
    else:
        print(i)
