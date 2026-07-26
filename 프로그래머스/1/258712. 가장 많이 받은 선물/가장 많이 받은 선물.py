def solution(friends, gifts):
    answer = 0
    gifts_score = {people: 0 for people in friends}
    gifts_history = {people: [0 for _ in range(len(friends))] for people in friends}
    friends_idx = {friends[i]: i for i in range(len(friends))}
    next_gifts = {people: 0 for people in friends}

    for gift in gifts:
        give_gift, receive_gift = gift.split()

        gifts_score[give_gift] += 1
        gifts_score[receive_gift] -= 1

        gifts_history[give_gift][friends_idx[receive_gift]] += 1

    for i in range(len(friends)-1):
        base_friend = friends[i]
        base_friend_idx = friends_idx[base_friend]

        for j in range(i+1, len(friends)):
            another_friend = friends[j]
            another_friend_idx = friends_idx[another_friend]

            if gifts_history[base_friend][another_friend_idx] > gifts_history[another_friend][base_friend_idx]:
                next_gifts[base_friend] += 1
            elif gifts_history[base_friend][another_friend_idx] < gifts_history[another_friend][base_friend_idx]:
                next_gifts[another_friend] += 1
            else:
                if gifts_score[base_friend] > gifts_score[another_friend]:
                    next_gifts[base_friend] += 1
                elif gifts_score[base_friend] < gifts_score[another_friend]:
                    next_gifts[another_friend] += 1

    return max(next_gifts.values())