def check_users(users, emoticons_price, emoticon_visited, discount):
    emo_plus_user = 0
    total_price = 0

    for dis, max_bill in users:
        sum_price = 0

        for emo_idx in range(len(emoticon_visited)):
            if discount[emoticon_visited[emo_idx]] >= dis:
                price = emoticons_price[emo_idx][emoticon_visited[emo_idx]]
                sum_price += price

        if sum_price >= max_bill:
            emo_plus_user += 1
        else:
            total_price += sum_price

    return emo_plus_user, total_price


def check_emo(users, emoticons_price, level, answer, emoticon_visited):
    if level == len(emoticons_price):
        discount = [10, 20, 30, 40]
        emo_plus_user, total_price = check_users(users, emoticons_price, emoticon_visited, discount)

        if emo_plus_user > answer[0]:
            answer = [emo_plus_user, total_price]
        elif emo_plus_user == answer[0] and total_price > answer[1]:
            answer = [emo_plus_user, total_price]

        return answer

    for i in range(4):
        emoticon_visited.append(i)

        answer = check_emo(users, emoticons_price, level+1, answer, emoticon_visited)

        emoticon_visited.pop()

    return answer



def solution(users, emoticons):
    answer = [0, 0]
    emoticons_price = [[0] * 4 for _ in range(len(emoticons))]

    for i in range(len(emoticons)):
        emoticons_price[i][0] = (emoticons[i] * 90) // 100
        emoticons_price[i][1] = (emoticons[i] * 80) // 100
        emoticons_price[i][2] = (emoticons[i] * 70) // 100
        emoticons_price[i][3] = (emoticons[i] * 60) // 100

    answer = check_emo(users, emoticons_price, 0, answer, [])

    return answer