def solution(message, spoiler_ranges):
    answer = 0
    message_idx = [0 for _ in range(len(message))]
    message_dict = dict()

    idx = 1

    for start, end in spoiler_ranges:
        for i in range(start, end+1):
            message_idx[i] = idx

        idx += 1

    words = set()
    message_list = message.split()

    for m in message_list:
        message_dict[m] = message_list.count(m)

    idx = 0

    for i in range(len(message)):
        if message[i] == ' ':
            idx += 1

        elif message_idx[i] > 0:
            words.add((message_list[idx], idx))

    word_list = []
    for word, _ in words:
        word_list.append(word)

    for word in set(word_list):
        if word_list.count(word) == message_dict[word]:
            answer += 1

    return answer


message_input = "my phone number is 01012345678 and may i have your phone number"
spoiler_ranges_input = 	[[5, 5], [25, 28], [34, 40], [53, 59]]

print(solution(message_input, spoiler_ranges_input))