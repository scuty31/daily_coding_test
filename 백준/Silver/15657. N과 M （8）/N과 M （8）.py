def print_a(level, n, m, a, idx, answer):
    if level >= m:
        result = ' '.join(list(map(str, answer)))
        print(result)
        return

    for i in range(idx, n):
        answer.append(a[i])
        print_a(level+1, n, m, a, i, answer)
        answer.pop()



def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    for i in range(n):
        answer = [a[i]]
        print_a(1, n, m, a, i, answer)


solution()
