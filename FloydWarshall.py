INF = 9999

def print_sol(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end = " ")
            else:
                print(distance[i][j], end = " ")
        print(" ")

def floydWarshall(nV, G): # time - O(V^3), space - O(V^2)
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    print_sol(nV, distance)

G = [[0,8,INF,1],
     [INF,0,1,INF],
     [4,INF,0,INF],
     [INF,2,9,1]]

floydWarshall(4,G)

