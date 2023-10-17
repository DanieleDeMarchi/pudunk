from player import read_players
from teams import read_teams
from dataset_creator import create_excel

def main():
   team_list = read_teams("teams.json")
   player_list = read_players("stats.json", team_list)
   player_list.extend(read_players("stats.json", team_list))
   player_list.extend(read_players("stats_2.json", team_list))
   player_list.extend(read_players("stats_3.json", team_list))
   player_list.extend(read_players("stats_4.json", team_list))
   player_list.extend(read_players("stats_5.json", team_list))
   player_list.extend(read_players("stats_6.json", team_list))
   player_list.extend(read_players("stats_7.json", team_list))
   create_excel(player_list)
   

if __name__ == "__main__":
    main()   