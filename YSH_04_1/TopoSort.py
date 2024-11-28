# 코드 10.11: 위상정렬
def topological_sort_AM(vertex, edge) :
    # 정점의 진입차수 리스트 inDeg 생성 및 초기화
    n = len(vertex)             # 정점의 개수
    inDeg = [0] * n             # inDeg: 진입차수 저장 리스트
    for i in range(n) :
        for j in range(n) :
            if edge[i][j]>0 :  # 모든 간선 <i,j>에 대해
                inDeg[j] += 1   # j의 진입차수를 1 증가

    # 진입차수가 0인 정점 리스트 생성 및 초기화
    vlist = []
    for i in range(n) :
        if inDeg[i]==0 :
            vlist.append(i)

    # 진입차수가 0인 정점이 더 이상 없을 때 까지 위상 정렬
    while len(vlist) > 0 :
        v = vlist.pop()                 # 진입차수가 0인 정점을 꺼냄
        print(vertex[v], end=' ')       # 화면 출력(방문, 또는 수강)

        for u in range(n) :
            if v!=u and edge[v][u]>0:  # 간선 <v,u>가 있으면
                inDeg[u] -= 1           # u의 진입차수 감소
                if inDeg[u] == 0 :      # u의 진입차수가 0이면
                    vlist.append(u)     # u를 vlist에 추가



vertex = ['A', 'B', 'C', 'D', 'E', 'F' ]
adj =  [ [ 0,   0,   1,   1,   0,   0 ],
         [ 0,   0,   0,   1,   1,   0 ],
         [ 0,   0,   0,   1,   0,   1 ],
         [ 0,   0,   0,   0,   0,   1 ],
         [ 0,   0,   0,   0,   0,   1 ],
         [ 0,   0,   0,   0,   0,   0 ] ]
print('topological_sort: ')
topological_sort_AM(vertex, adj)
print()