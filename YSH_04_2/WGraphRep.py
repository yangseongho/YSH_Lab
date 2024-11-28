# 코드 11.1: 인접 행렬을 이용한 가중치 그래프 표현
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]


# 코드 11.2: 가중치 그래프의 가중치 합(인접 행렬)
def weightSum( vlist, W ):				# 매개변수: 정점 리스트, 인접 행렬
    sum = 0							# 가중치의 합
    for i in range(len(vlist)) :		# 모든 정점에 대해(i: 0, ... N-1)
        for j in range(i+1, len(vlist)) :	# 하나의 행에 대해 (삼각영역)
            if W[i][j] != None :		# 만약 간선이 있으면
                sum += W[i][j]			# sum에 추가
    return sum							# 전체 가중치 합을 반환


# 코드 11.3: 가중치 그래프의 모든 간선 출력(인접 행렬)
def printAllEdges(vlist, W ):			# 매개변수: 정점 리스트, 인접 행렬
    for i in range(len(vlist)) :
        for j in range(i+1, len(W[i])) :		# 모든 간선 W[i][j]에 대해
            if W[i][j] != None and W[i][j] != 0 :	# 간선이 있으면
                print("(%s,%s,%d)"%(vlist[i],vlist[j],W[i][j]), end=' ')
    print()


print('AM : weight sum = ', weightSum(vertex, weight))
printAllEdges(vertex, weight)


# 코드 11.4: 딕셔너리와 집합을 이용한 가중치 그래프
graphAL={'A': {('B',29),('F',10)          },
        'B' : {('A',29),('C',16), ('G',15)},
        'C' : {('B',16),('D',12)          },
        'D' : {('C',12),('E',22), ('G',18)},
        'E' : {('D',22),('F',27), ('G',25)},
        'F' : {('A',10),('E',27)          },
        'G' : {('B',15),('D',18), ('E',25)} }


# 코드 10.5: 가중치 그래프의 가중치 합(인접 리스트)
def weightSum(graph):			# 가중치의 총 합을 구하는 함수
    sum = 0
    for v in graph:             # 그래프의 모든 정점 v에 대해: 'A', 'B', ...
        for e in graph[v]:      # v의 모든 간선 e에 대해: ('B', 29), ...
            sum += e[1]			# sum에 추가
    return sum//2				# 하나의 간선이 두 번 더해지므로 2로 나눔

# 코드 11.6: 가중치 그래프의 모든 간선 출력(인접 리스트)
def printAllEdges(graph):		# 모든 간선을 출력하는 함수
    for v in graph:             # 그래프의 모든 정점 v에 대해: 'A', 'B', ...
        for e in graph[v]:      # v의 모든 간선 e에 대해: ('B', 29), ...
            if v <= e[0] :
                print("(%s,%s,%d)"%(v,e[0],e[1]), end=' ')

print('AL : weight sum = ', weightSum(graphAL))
printAllEdges(graphAL)