from collections import Counter

def solution(str1, str2):
    def make_list(s):
        s = s.lower()
        result = []

        for i in range(len(s) - 1):
            pair = s[i:i+2]

            if 'a' <= pair[0] <= 'z' and 'a' <= pair[1] <= 'z':
                result.append(pair)

        return result

    a = Counter(make_list(str1))
    b = Counter(make_list(str2))

    inter_size = sum((a & b).values())
    union_size = sum((a | b).values())

    answer = 0

    if union_size == 0:
        answer = 65536
    else:
        answer = int(inter_size / union_size * 65536)

    return answer


print(solution('aa1+aa2', 'AAAA12'))