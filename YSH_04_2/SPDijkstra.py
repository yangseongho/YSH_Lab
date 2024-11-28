
# 코드 11.13: 최단 정점 선택 함수
INF = 999
def choose_vertex(dist, found) :
    min = INF
    minpos = -1

    for i in range(len(dist)) :
        if dist[i]< min and found[i]==False :
            min = dist[i]
            minpos = i
    return minpos;

# 코드 11.14: Dijkstra 알고리즘
def shortest_path_dijkstra(vertex, adj, start) :
    vsize = len(vertex)
    dist = list(adj[start])
    path = [start] * vsize
    found= [False] * vsize

    found[start] = True;
    dist[start] = 0;

    for i in range(vsize) :
        print("Step%2d: "%(i+1), dist)  # 단계별 dist[] 출력용
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize) :
            if not found[w] :
                if (dist[u] + adj[u][w] < dist[w]) :
                    dist[w] = dist[u] + adj[u][w];
                    path[w] = u;

    return path


# 코드 11.15: Dijkstra 알고리즘 테스트 프로그램
if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
    weight = [ [0,	    7,		INF,	INF,	3,      10,		INF],
               [7,		0,	    4,		10,	    2,	    6,	    INF],
               [INF,	4,		0,	    2,		INF,	INF,	INF],
               [INF,	10,     2,		0,      11,		9,	    4   ],
               [3,	    2,	    INF,   11,		0,      13,		5   ],
               [10,		6,	    INF,	9,      13,		0,	    INF],
               [INF,    INF,	INF,   4,		5,		INF,	0   ]]

    print("Shortest Path By Dijkstra Algorithm")
    start = 0
    path = shortest_path_dijkstra(vertex, weight, start)

    for end in range(len(vertex)) :
        if end != start :
            print("[최단경로: %s->%s] %s" %(vertex[start], vertex[end], vertex[end]), end='')
            while (path[end] != start) :
                print(" <- %s" % vertex[path[end]], end='')
                end = path[end]
            print(" <- %s" % vertex[path[end]])


