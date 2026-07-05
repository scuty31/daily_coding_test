def DFS(banned_id_count, visited, level, answer):
    if level >= len(banned_id_count):
        answer.add(tuple(sorted(visited)))
        return

    for i in range(len(banned_id_count[level])):
        if banned_id_count[level][i] in visited:
            continue

        visited.append(banned_id_count[level][i])
        DFS(banned_id_count, visited, level+1, answer)
        visited.pop()


def solution(user_id, banned_id):
    answer = set()
    banned_id_count = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        banned = banned_id[i]

        for j in range(len(user_id)):
            if len(banned) == len(user_id[j]):
                is_banned_id = True

                for k in range(len(banned)):
                    if (banned[k] != '*') and (banned[k] != user_id[j][k]):
                        is_banned_id = False
                        break

                if is_banned_id:
                    banned_id_count[i].append(j)

    DFS(banned_id_count, [], 0, answer)

    return len(answer)


user_id_input = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_input = ["*rodo", "*rodo", "******"]

print(solution(user_id_input, banned_id_input))