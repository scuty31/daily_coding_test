def check(s1, s2):
    prefix_chr = []
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix_chr.append(s1[i])
        else:
            break

    return "".join(prefix_chr)


n = int(input())
l = []
for i in range(n):
    s = input().rstrip()
    l.append((s, i))

l.sort()
prefix_dict = dict()
max_length = 0
prefix_list = []
for i in range(1, n):
    prefix = check(l[i][0], l[i-1][0])
    prefix_len = len(prefix)
    if prefix_len < max_length:
        continue

    if prefix_len > max_length:
        prefix_list = []
        max_length = prefix_len

    prefix_list.append(prefix)
    if prefix not in prefix_dict:
        prefix_dict[prefix] = set()

    prefix_dict[prefix].add((l[i][1], l[i][0]))
    prefix_dict[prefix].add((l[i-1][1], l[i-1][0]))


ans_idx = n
ans = None
for prefix_word in prefix_list:
    first, second = sorted(prefix_dict[prefix_word])[:2]
    if first[0] < ans_idx:
        ans = (first[1], second[1])
        ans_idx = first[0]

print(ans[0])
print(ans[1])