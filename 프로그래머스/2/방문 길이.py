def solution(dirs):
   answer = 0
   dx = [-1, 1, 0, 0]
   dy = [0, 0, 1, -1]
   visited = []
   dirs_dic = {'U':0, 'D':1, 'R':2, 'L':3}
   x, y = 0, 0

   for d in dirs:
      dn = dirs_dic[d]
      nx, ny = x + dx[dn], y+dy[dn]

      if nx < -5 or ny < -5 or nx > 5 or ny > 5:
         continue
      if (x, y, nx, ny) not in visited:
         visited.append((x, y, nx, ny))
         visited.append((nx, ny, x, y))
         answer += 1

      x, y = nx, ny

   return answer


input_dirs = 'LULLLLLLU'
print(solution(input_dirs))