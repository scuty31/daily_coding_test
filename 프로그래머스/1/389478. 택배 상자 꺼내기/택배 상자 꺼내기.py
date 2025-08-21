def zigzag_box(rows, cols, n):
    boxes = [[0] * cols for _ in range(rows+1)]
    num = 1
    i = 0

    for i in range(rows+1):
        if i % 2 == 0:  # 짝수 행은 왼쪽 → 오른쪽
            for j in range(cols):
                if num > n:
                    break

                boxes[i][j] = num
                num += 1

        else:  # 홀수 행은 오른쪽 → 왼쪽
            for j in range(cols - 1, -1, -1):
                if num > n:
                    break

                boxes[i][j] = num
                num += 1

    return boxes


def select_box(num, boxes):
    for x in range(len(boxes)):
        for y in range(len(boxes[x])):
            if boxes[x][y] == num:
                return x, y


def solution(n, w, num):
    answer = 0
    boxes = zigzag_box(n // w, w, n)

    num_x, num_y = select_box(num, boxes)

    if num > (w * (n//w)):
        answer = 1
    else:
        answer = (n//w) - num_x

        if boxes[n//w][num_y] != 0:
            answer += 1

    return answer
