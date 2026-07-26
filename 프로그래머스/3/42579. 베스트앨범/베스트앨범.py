def solution(genres, plays):
    answer = []
    genres_set = set(genres)
    genres_dict = {i: 0 for i in genres_set}

    for i in range(len(genres)):
        genres_dict[genres[i]] += plays[i]

    play_list = []

    for i in range(len(genres)):
        song = [i, genres[i], genres_dict[genres[i]], plays[i]]
        play_list.append(song)

    play_list.sort(key=lambda x:(x[2],x[3]), reverse = True)

    genres_count = {i: 0 for i in genres_set}

    for idx, genre, _, _ in play_list:
        if genres_count[genre] == 2:
            continue
        else:
            answer.append(idx)
            genres_count[genre] += 1

    return answer