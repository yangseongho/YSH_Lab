# 코드 10.1: 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          # 현재 정점 s를 출력함
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면
                DFS(vtx, adj, v, visited)


# 코드 10.2: 깊이 우선 탐색 테스트 프로그램
vtx =  ['A', 'B','C','D','E','F','G','H']
edge = [ [  0,  1,  1,  0,  0,  0,  0,  0],
         [  1,  0,  0,  1,  0,  0,  0,  0],
         [  1,  0,  0,  1,  1,  0,  0,  0],
         [  0,  1,  1,  0,  0,  1,  0,  0],
         [  0,  0,  1,  0,  0,  0,  1,  1],
         [  0,  0,  0,  1,  0,  0,  0,  0],
         [  0,  0,  0,  0,  1,  0,  0,  1],
         [  0,  0,  0,  0,  1,  0,  1,  0] ]

print('DFS(출발:A) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()


# 코드 10.5: 딕셔너리와 집합으로 표현된 그래프의 깊이우선탐색
def DFS2(graph, v, visited):
    if v not in visited :           # v가 방문되지 않았으면
        visited.add(v)              # v를 방문했다고 표시
        print(v, end=' ')           # v를 출력
        nbr = graph[v] - visited    # v의 인접 정점 리스트
        for u in nbr:               # v의 모든 인접 정점에 대해
            DFS2(graph, u, visited)  # 순환 호출

# 코드 10.6: DFS2 테스트 프로그램
mygraph = { "A" : {"B","C"},
            "B" : {"A", "D"},
            "C" : {"A", "D", "E"},
            "D" : {"B", "C", "F"},
            "E" : {"C", "G", "H"},
            "F" : {"D"},
            "G" : {"E", "H"},
            "H" : {"E", "G"}
          }

print('DFS2(출발:A) : ', end="")
DFS2(mygraph, "A", set())
print()
