INF = 9999

def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end="")
            else:
                print("%4d " % A[i][j], end="")
        print("")

def reconstruct_path(start, end, path, vertex):
    if path[start][end] == -1:
        return None
    route = []
    while start != end:
        route.append(vertex[start])
        start = path[start][end]
    route.append(vertex[end])
    return route

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수
    A = [list(row) for row in adj]  # 2차원 배열 복사
    path = [[-1 if adj[i][j] == INF or i == j else j for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[i][k]  # 경로 갱신
        printA(A)  # 진행상황 출력용

    return A, path

if __name__ == "__main__":
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0]
    ]

    print("Shortest Path By Floyd's Algorithm")
    A, path = shortest_path_floyd(vertex, weight)

    # 사용자 입력으로 시작 정점과 끝 정점 받아 최단 경로와 거리 출력
    while True:
        start_vertex = input("\nStart Vertex (or 'exit' to quit): ").strip()
        if start_vertex.lower() == 'exit':
            break
        end_vertex = input("End Vertex: ").strip()

        if start_vertex not in vertex or end_vertex not in vertex:
            print("Invalid vertices. Please try again.")
            continue

        start_idx = vertex.index(start_vertex)
        end_idx = vertex.index(end_vertex)

        if A[start_idx][end_idx] == INF:
            print(f"No path exists between {start_vertex} and {end_vertex}.")
        else:
            path_list = reconstruct_path(start_idx, end_idx, path, vertex)
            distance = A[start_idx][end_idx]
            print(f"\n* Shortest Path: {' -> '.join(path_list)}")
            print(f"* Distance of the Shortest Path: {distance}")
