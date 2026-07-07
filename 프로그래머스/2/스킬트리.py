def check_skill(skill_list, skill_tree):
    idx = 0
    visited = dict()

    for s in skill_tree:
        if s in skill_list:
            if skill_list[idx] == s:
                visited[s] = 1
                idx += 1
            elif visited.get(s):
                continue
            else:
                return False

    return True


def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    skill_tree_list = []

    for i in range(len(skill_trees)):
        skill_tree_list.append(list(skill_trees[i]))

    for i in range(len(skill_trees)):
        if check_skill(skill_list, skill_tree_list[i]):
            answer += 1

    return answer


skill_input = "CBD"
skill_trees_input = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill_input, skill_trees_input))