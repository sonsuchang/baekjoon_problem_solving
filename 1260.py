import sys
N, M, V = map(int, sys.stdin.readline().split())
search_dict = {}
for _ in range(M):
    M_f, M_s = map(int, sys.stdin.readline().split())
    if M_f in search_dict.keys():
        search_dict[M_f].append(M_s)
    else:
        search_dict[M_f] = [M_s]
print(search_dict)