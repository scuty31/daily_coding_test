
def solution():
	n = int(input())
	score_team = dict()
	rate = list(map(int, input().split()))

	for i in range(n):
		if score_team.get(rate[i]):
			score_team[rate[i]] += 1
		else:
			score_team[rate[i]] = 1

	team = [[1e9, 1e9] for _ in range(len(score_team) + 1)]
	fifth_player = [1e9 for _ in range(len(score_team) + 1)]

	for i in score_team.keys():
		if score_team[i] >= 6:
			team[i] = [0, 0]

	now_score = 1
	for j in range(n):
		if score_team[rate[j]] >= 6:
			team[rate[j]][1] += 1

			if team[rate[j]][1] <= 4:
				team[rate[j]][0] += now_score

			if team[rate[j]][1] == 5:
				fifth_player[rate[j]] = now_score

			now_score += 1

	winner = team.index(min(team))

	if team.count(min(team)) == 1:
		return winner

	else:
		winner_score = min(team)

		for k in range(len(score_team)+1):
			if team[k] != winner_score:
				fifth_player[k] = 1e9

		return fifth_player.index(min(fifth_player))


t = int(input())

for _ in range(t):
	print(solution())