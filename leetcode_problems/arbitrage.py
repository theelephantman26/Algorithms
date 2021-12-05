import math
import copy

def findArbitrage(adjMat, currencies):
    exchange_matrix = copy.deepcopy(adjMat)
    flag = False
    path_matrix = []
    for i in range(currencies):
        path_matrix.append([])
        for j in range(currencies):
            path_matrix[i].append([])
            path_matrix[i][j].append(i)
    path_matrix_temp = copy.deepcopy(path_matrix)
    max_cost = -1
    ans_k = 0
    best_path = []
    for k in range(0,currencies):
        for i in range(0, currencies):
            for j in range(0, currencies):
                if adjMat[i][j] < adjMat[i][k]*adjMat[k][j]:
                    flag = True
                    exchange_matrix[i][j] = adjMat[i][k]*adjMat[k][j]
                    path_matrix_temp[i][j] = path_matrix[i][k] + path_matrix[k][j]
        adjMat = copy.deepcopy(exchange_matrix)
        path_matrix = copy.deepcopy(path_matrix_temp)
        if flag:
            for i in range(currencies):
                if adjMat[i][i] > max_cost:
                    max_cost = adjMat[i][i]
                    best_path = path_matrix[i][i].copy()
                    best_path.append(i)
            break
    return (ans_k, max_cost, best_path)

def checkArbitrage(adjMat, currencies):
    for k in range(currencies):
        for i in range(currencies):
            for j in range(currencies):
                if adjMat[i][j] < adjMat[i][k]*adjMat[k][j]:
                    adjMat[i][j] = adjMat[i][k]*adjMat[k][j]
        for i in range(currencies):
            if adjMat[i][i] > 1:
                return True
    return False

adjMat = [[1,2,0],[0,1,2.5],[0.2,0,1]]
print(findArbitrage(adjMat,3))
