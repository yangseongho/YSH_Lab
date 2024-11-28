from queue import Queue

# 그래프 입력
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edge = ['A-B', 'A-C', 'B-D', 'C-D', 'C-E', 'D-F', 'E-H', 'E-G', 'G-H']

# 인접 리스트 생성
adj_list = {v: [] for v in vertex}
for e in edge:
    u, v = e.split('-')
    adj_list[u].append(v)
    adj_list[v].append(u)

# 인접 행렬 생성
n = len(vertex)
vertex_idx = {v: i for i, v in enumerate(vertex)}
adj_matrix = [[0] * n for _ in range(n)]
for e in edge:
    u, v = e.split('-')
    adj_matrix[vertex_idx[u]][vertex_idx[v]] = 1
    adj_matrix[vertex_idx[v]][vertex_idx[u]] = 1

# DFS 구현
def dfs(vtx, adj, v, visited):
    visited.add(v)
    result.append(v)
    for neighbor in adj[v]:
        if neighbor not in visited:
            dfs(vtx, adj, neighbor, visited)

# BFS 구현
def bfs(vtx, adj, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)
    result = []

    while not queue.empty():
        v = queue.get()
        result.append(v)
        for neighbor in adj[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)
    return result

# 연결 성분 계산
def connected_components(vtx, adj):
    visited = set()
    components = []

    for v in vtx:
        if v not in visited:
            global result
            result = []
            dfs(vtx, adj, v, visited)
            components.append(result)

    return components

# Spanning Tree 계산
def spanning_tree(vtx, adj, v):
    visited = set()
    edges = []

    def dfs_spanning(v):
        visited.add(v)
        for neighbor in adj[v]:
            if neighbor not in visited:
                edges.append((v, neighbor))
                dfs_spanning(neighbor)

    dfs_spanning(v)
    return edges

# 그래프 입력받기
vertex_input = input("Vertex (예시: A, B, C, ...): ")
edge_input = input("Edge (예시: A-B, A-C, ...): ")

# Vertex와 Edge 리스트로 변환
vertex = [v.strip() for v in vertex_input.split(",")]
edge = [e.strip() for e in edge_input.split(",")]

# Adjacent List 생성
adj_list = {v: [] for v in vertex}  # 초기화
for e in edge:
    u, v = e.split("-")  # 간선 분리
    adj_list[u].append(v)  # 양방향 연결
    adj_list[v].append(u)

# 출력
print("\nVertex List: ", vertex)
print("Edge List: ", edge)
print("Adjacent Vertex List: ", adj_list)


# DFS 실행
result = []
dfs(vertex, adj_list, 'A', set())
print("DFS: ", " - ".join(result))

# BFS 실행
bfs_result = bfs(vertex, adj_list, 'A')
print("BFS: ", " - ".join(bfs_result))

# 연결 성분 계산
cc = connected_components(vertex, adj_list)
print("Connected Components: ", [" - ".join(c) for c in cc])

# Spanning Tree 계산
spanning_edges = spanning_tree(vertex, adj_list, 'A')
print("Spanning Tree Edges: ", spanning_edges)