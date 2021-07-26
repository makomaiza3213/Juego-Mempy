import os.path as path
import json


def no_encontre(nom):
    with open("scores.json") as file:
        data = json.load(file)
    i = 0
    ok = True
    while i < len(data) and ok:
        if data[i][0] != nom:
            i += 1
        else:
            ok = False
    return ok


def file_scores(player):
    if not path.exists("scores.json"):
        player_score = [[player.nick, 0, 0, 0, 0]]
        with open("scores.json", "w") as file:
            json.dump(player_score, file, indent=4)
    else:
        if no_encontre(player.nick):
            with open("scores.json") as file:
                data = json.load(file)
                player_score = [player.nick, 0, 0, 0, 0]
                data.append(player_score)
            with open("scores.json", "w") as file:
                json.dump(data, file, indent=4)


def update_scores_levels(player, data, i):
    if player.nivel_actual == "1":
        if data[i][1] < player.puntaje:
            data[i][1] = player.puntaje
    elif player.nivel_actual == "2":
        if data[i][2] < player.puntaje:
            data[i][2] = player.puntaje
    elif player.nivel_actual == "3":
        if data[i][3] < player.puntaje:
            data[i][3] = player.puntaje
    else:
        if data[i][4] < player.puntaje:
            data[i][4] = player.puntaje
    return data


def update_scores(player):
    with open("scores.json") as file:
        data = json.load(file)
    i = 0
    while i <= len(data):
        if data[i][0] == player.nick:
            new = update_scores_levels(player, data, i)
            break
        i += 1
    with open("scores.json", "w") as file:
        json.dump(new, file, indent=4)


def new_lists_with_corresponding_scores():
    with open("scores.json") as file:
        scores = json.load(file)
    scores.sort(key=lambda x: x[1])
    level1 = list(reversed(scores))

    scores.sort(key=lambda x: x[2])
    level2 = list(reversed(scores))
    l2 = []
    for player in range(0, len(level2)):
        new2 = [level2[player][0], level2[player][2]]
        l2.append(new2)

    scores.sort(key=lambda x: x[3])
    level3 = list(reversed(scores))
    l3 = []
    for player in range(0, len(level3)):
        new3 = [level3[player][0], level3[player][3]]
        l3.append(new3)

    scores.sort(key=lambda x: x[4])
    level4 = list(reversed(scores))
    l4 = []
    for player in range(0, len(level4)):
        new4 = [level4[player][0], level4[player][4]]
        l4.append(new4)

    return [level1, l2, l3, l4]
