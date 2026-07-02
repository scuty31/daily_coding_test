def solution(land):
    visited = [[0]*len(land[0]) for _ in range(len(land))]

    for i in range(len(land[0])):
        visited[0][i] = land[0][i]

    for idx in range(1, len(land)):
        visited[idx][0] = max(visited[idx-1][1], visited[idx-1][2], visited[idx-1][3]) + land[idx][0]
        visited[idx][1] = max(visited[idx - 1][0], visited[idx - 1][2], visited[idx - 1][3]) + land[idx][1]
        visited[idx][2] = max(visited[idx - 1][0], visited[idx - 1][1], visited[idx - 1][3]) + land[idx][2]
        visited[idx][3] = max(visited[idx - 1][0], visited[idx - 1][1], visited[idx - 1][2]) + land[idx][3]

    answer = max(visited[-1])

    return answer


land_input = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land_input))