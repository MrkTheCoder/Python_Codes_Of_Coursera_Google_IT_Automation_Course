#!/usr/bin/env python3
#   This script requires the 'gamers.log' file. You can download it from this location:
#         http
#   If you're unable to download it, here's the complete content of the 'gamers.log':
# [2023/12/12][09:30 AM]: WIN Fortnite  # 123 (Alpha_Gamer)
# [2023/12/12][02:45 PM]: LOSE League of Legends  # 45 (BetaPlayer)
# [2023/12/12][07:15 PM]: WIN Valorant  # 123 (Alpha_Gamer)
# [2023/12/13][10:00 AM]: LOSE Fortnite  # 89 (DeltaPlayer)
# [2023/12/13][03:20 PM]: WIN Apex Legends  # 155 (EpsilonGamer)
# [2023/12/13][08:45 PM]: LOSE Minecraft(ZetaPlayer)
# [2023/12/14][11:10 AM]: WIN Counter-Strike(EtaGamer)
# [2023/12/14][04:55 PM]: LOSE Call of Duty  # 72 (Theta_Player)
# [2023/12/14][09:25 PM]: WIN Warframe  # 89 (DeltaPlayer)
# [2023/12/15][12:40 PM]: LOSE Fortnite(KappaPlayer)
# [2023/12/15][06:05 PM]: WIN Counter-Strike  # 177 (LambdaGamer)
# [2023/12/15][10:30 PM]: LOSE PUBG(RhoGamer)
# [2023/12/16][01:15 PM]: WIN Warframe  # 123 (Alpha_Gamer)
# [2023/12/16][07:50 PM]: LOSE Counter-Strike  # 188 (XiPlayer)
# [2023/12/16][11:55 PM]: WIN Fortnite 2  # 89 (DeltaPlayer)
# [2023/12/17][02:25 PM]: LOSE The Witcher 3  # 113 (PiPlayer)
# [2023/12/17][08:15 PM]: WIN Warframe(RhoGamer)
# [2023/12/18][12:20 PM]: LOSE NBA 2K22(SigmaPlayer)
# [2023/12/18][05:40 PM]: WIN Red Dead Redemption 2  # 45 (BetaPlayer)
# [2023/12/18][09:45 PM]: LOSE Cyberpunk 2077 (SigmaPlayer)
import operator
import re
from collections import defaultdict


def parse_log_file(fullpath):
    games = defaultdict(int)
    players = defaultdict(lambda: {'WIN': 0, 'LOSE': 0})

    cp = re.compile(
        r'(?P<result>WIN|LOSE)(?P<game>[\w\s-]+)(?:[#\d]+)?\s\((?P<user>[\w.]+)\)')

    with open(fullpath) as reader:
        for line in reader:
            result = cp.search(line)
            if result:
                game_name = result.group('game').strip()
                game_result = result.group('result')
                player = result.group('user')

                players[player][game_result] += 1
                games[game_name] += 1

    sorted_games = sorted(
        games.items(), key=operator.itemgetter(1), reverse=True)

    sorted_users = [(key, dic['WIN'], dic['LOSE'])
                    for key, dic in sorted(players.items())]

    return sorted_users, sorted_games


if __name__ == '__main__':
    logfile_fullpath = 'gamers.log'
    users_list, game_list = parse_log_file(logfile_fullpath)

    print(f"{'Gamers list:':^28}")
    for user in users_list:
        print(f"{user[0]:<12}:  {user[1]} WIN, {user[2]} LOSE")

    print(f"\n{'Top games:':^32}")
    for game in game_list:
        print(f"{game[0]:>21}:  {game[1]} times")
