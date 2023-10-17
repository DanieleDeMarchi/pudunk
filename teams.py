import json


class Team:
    # "abbrev": "Ind",
    # "id": 11,
    # "location": "Indiana",
    # "name": "Pacers",
    def __init__(self, team_dict):
        self.abbrv = team_dict["abbrv"]
        self.id = team_dict["id"]
        self.location = team_dict["location"]
        self.name = team_dict["name"]

    def to_dict(self):
        return {"abbrv": self.abbrv, "id": self.id, "location": self.location, "name": self.name}



def main():
    teams = read_teams('teams.json')
    write_file(teams, 'teams_2.json')

def read_teams(path):
    with open(path, 'r') as file:
        data = json.load(file)

    teams_data = data.get("teams")
    teams = []

    for team_data in teams_data:
        teams.append(Team(team_data))
        
    return teams


def write_file(teams, path):
    data = {}
    data['teams'] = [team.to_dict() for team in teams]
    with open(path, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
