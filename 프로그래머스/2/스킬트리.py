def solution(skill, skill_trees):
    answer = 0
    skill_dict = {'': 1}

    for i in range(len(skill)):
        skill_dict[skill[:i+1]] = 1


    for skill_tree in skill_trees:
        filtered = []

        for s in skill_tree:
            if s in skill:
                filtered.append(s)

        filtered = ''.join(filtered)

        if skill_dict.get(filtered):
            answer += 1

    return answer


skill_input = "CBD"
skill_trees_input = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill_input, skill_trees_input))