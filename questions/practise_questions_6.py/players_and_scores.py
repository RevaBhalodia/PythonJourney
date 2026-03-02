def rank_players(scores):
    # Sort players by score (descending)
    sorted_players = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    ranks = {}
    rank = 0
    prev_score = None

    for player, score in sorted_players:
        if score != prev_score:
            rank += 1

        ranks[player] = rank
        prev_score = score

    return ranks

scores = {"A": 90, "B": 75, "C": 90, "D": 60}
result = rank_players(scores)

for player in sorted(result, key=lambda x: result[x]):
    print(player, "→ Rank", result[player])