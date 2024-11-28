# 코드 10.10: 깊이우선탐색을 이용한 신장트리
def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)


# 테스트 프로그램
vtx =  ['A', 'B','C','D','E','F','G','H']
edge = [ [  0,  1,  1,  0,  0,  0,  0,  0],
         [  1,  0,  0,  1,  0,  0,  0,  0],
         [  1,  0,  0,  1,  1,  0,  0,  0],
         [  0,  1,  1,  0,  0,  1,  0,  0],
         [  0,  0,  1,  0,  0,  0,  1,  1],
         [  0,  0,  0,  1,  0,  0,  0,  0],
         [  0,  0,  0,  0,  1,  0,  0,  1],
         [  0,  0,  0,  0,  1,  0,  1,  0] ]

print('신장트리(DFS): ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()