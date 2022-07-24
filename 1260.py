import sys
N, M, V = map(int, sys.stdin.readline().split())
search_dict = {}
for _ in range(M):
    M_f, M_s = map(int, sys.stdin.readline().split())
    if M_f not in search_dict.keys():
        search_dict[M_f] = [M_s]
    else:
        search_dict[M_f].append(M_s)

visited_dfs = []
def search_dfs(search_dict, V, visited_dfs):
    visited_dfs.append(V)
    if V in search_dict.keys():
        for i in search_dict[V]:
            if i not in visited_dfs:
                search_dfs(search_dict, i, visited_dfs)
search_dfs(search_dict, V, visited_dfs)
print(*visited_dfs)

visited_bfs = []
def search_bfs(search_dict, V, visited_bfs):
    visited_bfs.append(V)
    if V in search_dict.keys():
        for i in search_dict[V]:
            if i not in visited_bfs:
                visited_bfs.append(i)
search_bfs(search_dict, V, visited_bfs)
print(*visited_bfs)