import json
from typing import TypeAlias
from teams import Team

ListTeam: TypeAlias = list[Team]

class Player:
    def __init__(self, player_data, teams: ListTeam):
        self.id = player_data["id"]
        self.active = player_data["player"]["active"]
        self.default_position_id = player_data["player"]["defaultPositionId"]
        self.draft_ranks_by_rank_type = player_data["player"]["draftRanksByRankType"]
        self.first_name = player_data["player"]["firstName"]
        self.full_name = player_data["player"]["fullName"]
        self.injured = player_data["player"]["injured"]
        self.injury_status = player_data["player"]["injuryStatus"]
        self.jersey = player_data["player"]["jersey"]
        self.last_news_date = player_data["player"]["lastNewsDate"]
        self.pro_team_id = player_data["player"]["proTeamId"]
        self.team = next((t for t in teams if t.id == self.pro_team_id), None)
        self.season_outlook = player_data["player"]["seasonOutlook"]
        #self.ratings = player_data["ratings"]
        if(player_data["player"]["stats"][0].get('averageStats') is not None):
            self.last_year_stats = PlayerStats(player_data["player"]["stats"][0]['averageStats'])
        else:
            self.last_year_stats = None
        
        projected_stats_index = len(player_data["player"]["stats"]) -1
        if(player_data["player"]["stats"][projected_stats_index].get('averageStats') is not None):
            self.projected_stats = PlayerStats(player_data["player"]["stats"][projected_stats_index]['averageStats'])
        else:
            self.projected_stats = None

    def __str__(self):
        return f"Player ID: {self.id}\nFull Name: {self.full_name}\nActive: {self.active}\nDefault Position ID: {self.default_position_id}\nDraft Ranks: {self.draft_ranks_by_rank_type}\nInjured: {self.injured}\nInjury Status: {self.injury_status}\nJersey: {self.jersey}\nLast News Date: {self.last_news_date}\nLast Video Date: {self.last_video_date}\nPro Team ID: {self.pro_team_id}\nSeason Outlook: {self.season_outlook}\nStats: {self.stats}\nRatings: {self.ratings}"


class PlayerStats:
    def __init__(self, stats_data):
        self.PPG = stats_data.get("0")
        self.BLK = stats_data.get("1")
        self.STL = stats_data.get("2")
        self.AST = stats_data.get("3")
        self.OREB = stats_data.get("4")
        self.DREB = stats_data.get("5")
        self.REB = stats_data.get("6")
        self.FOUL = stats_data.get("9")
        self.TO = stats_data.get("11")
        self.FG = stats_data.get("13")
        self.FGA = stats_data.get("14")
        self.FT = stats_data.get("15")
        self.FTA = stats_data.get("16")
        self.THREEPTM = stats_data.get("17")
        self.THREEPTA = stats_data.get("18")
        self.FG_Percentage = stats_data.get("19")
        self.FT_Percentage = stats_data.get("20")
        self.THREEPT_Percentage = stats_data.get("21")
        self.eFG_Percentage = stats_data.get("22")
        self.MFG = stats_data.get("23")
        self.MFT = stats_data.get("24")
        self.M3PT = stats_data.get("25")
        self.AST_DBL = stats_data.get("26")
        self.BLK_DBL = stats_data.get("27")
        self.MPG = stats_data.get("28")
        self.PPG_2 = stats_data.get("29")
        self.REB_2 = stats_data.get("30")
        self.STL_2 = stats_data.get("31")
        self.TO_2 = stats_data.get("32")
        self.FT_Percentage_2 = stats_data.get("33")
        self.A_TO = stats_data.get("35")
        self.Dbl_Dbl = stats_data.get("37")
        self.Trp_Dbl = stats_data.get("38")
        self.MPG_2 = stats_data.get("40")
        self.Started = stats_data.get("41")
        self.PG = stats_data.get("42")
        self.WIN_Percentage = stats_data.get("43")
        self.FT_Rate = stats_data.get("44")

    def __str__(self):
        return f"PPG: {self.PPG}\nBLK: {self.BLK}\nSTL: {self.STL}\nAST: {self.AST}\nOREB: {self.OREB}\nDREB: {self.DREB}\nREB: {self.REB}\nFOUL: {self.FOUL}\nTO: {self.TO}\nFG: {self.FG}\nFGA: {self.FGA}\nFT: {self.FT}\nFTA: {self.FTA}\n3PTM: {self.THREEPTM}\n3PTA: {self.THREEPTA}\nFG%: {self.FG_Percentage}\nFT%: {self.FT_Percentage}\n3PT%: {self.THREEPT_Percentage}\neFG%: {self.eFG_Percentage}\nMFG: {self.MFG}\nMFT: {self.MFT}\nM3PT: {self.M3PT}\nAST (Duplicate): {self.AST_DBL}\nBLK (Duplicate): {self.BLK_DBL}\nMPG: {self.MPG}\nPPG (Duplicate): {self.PPG_2}\nREB (Duplicate): {self.REB_2}\nSTL (Duplicate): {self.STL_2}\nTO (Duplicate): {self.TO_2}\nFT% (Duplicate): {self.FT_Percentage_2}\nA/TO: {self.A_TO}\nDbl-Dbl: {self.Dbl_Dbl}\nTrp-Dbl: {self.Trp_Dbl}\nMPG (Duplicate): {self.MPG_2}\nStarted: {self.Started}\nPG: {self.PG}\nWIN%: {self.WIN_Percentage}\nFT Rate: {self.FT_Rate}"


def read_players(path: str, teams: ListTeam):
    with open(path, 'r') as file:
       data = json.load(file)

    players_data = data.get("players")
    players = []

    for player_data in players_data:
        players.append(Player(player_data, teams))
    
    return players


def main():
    pass

if __name__ == "__main__":
    main()   