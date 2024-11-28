# 코드 10.3: 너비 우선 탐색(인접 리스트 방식)
from queue import Queue                 # queue 모듈의 Queue 사용
def BFS_AL(vtx, aList, s):
    n = len(vtx)                        # 그래프의 정점 수
    visited = [False]*n                 # 방문 확인을 위한 리스트
    Q = Queue()                         # 공백상태의 큐 생성
    Q.put(s)                            # 맨 처음에는 시작 정점만 있음
    visited[s] = True                   # s는 "방문"했다고 표시
    while not Q.empty() :
        s = Q.get()                     # 큐에서 정점을 꺼냄
        print(vtx[s], end=' ')          # 정점을 출력(처리)함
        for v in aList[s] :               # s의 모든 이웃 v에 대해
            if visited[v]==False :      # 방문하지 않은 이웃 정점이면
                Q.put(v)                # 큐에 삽입
                visited[v] = True       # "방문"했다고 표시


# 코드 10.4: 너비 우선 탐색 테스트 프로그램
vtx = [ 'A','B','C','D','E','F','G','H']
aList = [[ 1, 2 ],      # 'A'의 인접정점 인덱스
         [ 0, 3 ],      # 'B'의 인접정점 인덱스
         [ 0, 3, 4 ],   # 'C'
         [ 1, 2, 5 ],   # 'D'
         [ 2, 6, 7 ],   # 'E'
         [ 3 ],         # 'F'
         [ 4, 7 ],      # 'G'
         [ 4, 6 ] ]     # 'H'

print('BFS_AL(출발:A): ', end="")
BFS_AL(vtx, aList, 0)
print()
