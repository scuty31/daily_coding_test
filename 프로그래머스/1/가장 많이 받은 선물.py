def solution(friends, gifts):
    answer = 0
    gifts_score = {people: 0 for people in friends}                                         # 선물 지수
    gifts_history = {people: [0 for _ in range(len(friends))] for people in friends}        # 선물을 준 횟수
    friends_idx = {friends[i]: i for i in range(len(friends))}                              # 사람들의 index
    next_gifts = {people: 0 for people in friends}                                          # 다음달 몇개를 받을지

    # 이번 달까지 선물을 몇개 주고 받았는지 계산
    for gift in gifts:
        give_gift, receive_gift = gift.split()

        gifts_score[give_gift] += 1
        gifts_score[receive_gift] -= 1

        gifts_history[give_gift][friends_idx[receive_gift]] += 1

    # 다음달에 선물을 몇개 받을지 계산
    for i in range(len(friends)-1):
        base_friend = friends[i]
        base_friend_idx = friends_idx[base_friend]

        for j in range(i+1, len(friends)):
            another_friend = friends[j]
            another_friend_idx = friends_idx[another_friend]

            # 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람을 파악하고 더 많은 선물을 준 사람이 선물을 받음.
            if gifts_history[base_friend][another_friend_idx] > gifts_history[another_friend][base_friend_idx]:
                next_gifts[base_friend] += 1
            elif gifts_history[base_friend][another_friend_idx] < gifts_history[another_friend][base_friend_idx]:
                next_gifts[another_friend] += 1

            # 이번 달까지 두 사람 사이에 준 선물이 같거나 없는 경우
            else:
                # 선물 지수가 더 높은 사람이 선물을 받는다.
                if gifts_score[base_friend] > gifts_score[another_friend]:
                    next_gifts[base_friend] += 1
                elif gifts_score[base_friend] < gifts_score[another_friend]:
                    next_gifts[another_friend] += 1

    return max(next_gifts.values())


friends_input = ["muzi", "ryan", "frodo", "neo"]
gifts_input = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends_input, gifts_input))