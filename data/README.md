# Data

`player_matches.csv`: one row per player per league match, 144 forwards, Premier League, La Liga, Bundesliga and
Serie A, seasons 2000/01 to 2023/24 (33,678 rows).

| Column | Meaning |
|---|---|
| `name_player` | Player slug |
| `name_team`, `name_opp` | The player's team and the opponent |
| `name_league` | `premier-league`, `la-liga`, `bundesliga` or `serie-a` |
| `season` | Season, e.g. `2015/16` |
| `season_nbr` | Seasons the player already played in the source data (0 = his first); counts seasons present, not calendar years. The source has more rows than this file, so a few players start above 0 or skip a number |
| `matchday` | Matchday within the season (1 to 38) |
| `kick_off` | Match date |
| `home_pitch` | 1 if the player's team plays at home |
| `points_diff` | League points of the player's team minus the opponent's, before the match |
| `goal_balance_diff` | Goal difference of the player's team minus the opponent's, before the match |
| `goals_in_match` | Goals the player scored in the match |
| `goal` | 1 if the player scored at least once |

Source: Soccer Factor Model dataset, [github.com/AlexAndorra/football-modeling](https://github.com/AlexAndorra/football-modeling),
from Andorra & Göbel (2024), *Unveiling True Talent: The Soccer Factor Model for Skill Evaluation*,
[arXiv:2412.05911](https://arxiv.org/abs/2412.05911). Trimmed to the columns used here.
