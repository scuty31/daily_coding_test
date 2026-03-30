def print_list(n, m, step, arr, idx, visited):
    if step == m:
        print(' '.join(list(map(str, visited))))
        return

    for i in range(idx, len(arr)):
        visited.append(arr[i])
        print_list(n, m, step+1, arr, i, visited)
        visited.pop()


def solution():
    n, m = map(int, input().split())
    arr = list(set(map(int, input().split())))
    arr.sort()

    print_list(n, m, 0, arr, 0, [])


solution()