def solution(clothes):
    answer = 1
    clothes_dict = {}

    for cloth, part in clothes:
        if clothes_dict.get(part):
            clothes_dict[part] += 1
        else:
            clothes_dict[part] = 2      # 아무것도 입지 않는 것도 추가

    for part, cnt in clothes_dict.items():
        answer *= cnt

    answer -= 1     # 아무것도 입지 않은 경우 제거

    return answer


clothes_input = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes_input))