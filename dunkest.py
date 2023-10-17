from player import read_players
from teams import read_teams
from dataset_creator import create_excel

def main():
   team_list = read_teams("teams.json")
   player_list = read_players("stats.json", team_list)
   create_excel(player_list)
       




if __name__ == "__main__":
    main()   