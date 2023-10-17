import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.styles import Font
from player import Player
from typing import List

def create_excel(players, path="export.xlsx"):
   wb = Workbook()
   ws: Worksheet = wb.active
   player: Player
   row = [
         "Name",
         "POS",
         "TEAM",
         "PG",
         "MPG",
         "PPG",
         "AST",
         "REB",
         "TO",
         "BLK",
         "STL",
         "MFG",
         "MFT",
         "THREEPT_Percentage",
         "THREEPTA",
         "dd%",
         "trd%"
      ]
   ws.append(row)
   for x, player in enumerate(players):
      row = [
         player.full_name,
         "POS",
         player.team.abbrv,
         player.projected_stats.PG,
         player.projected_stats.MPG,
         player.projected_stats.PPG,
         player.projected_stats.AST,
         player.projected_stats.REB,
         player.projected_stats.TO,
         player.projected_stats.BLK,
         player.projected_stats.STL,
         player.projected_stats.MFG,
         player.projected_stats.MFT,
         player.projected_stats.THREEPT_Percentage,
         player.projected_stats.THREEPTA,
         player.last_year_stats.Dbl_Dbl if player.last_year_stats is not None else "",
         player.last_year_stats.Trp_Dbl if player.last_year_stats is not None else ""
      ]
   
      ws.append(row)
   
   wb.save(path)
