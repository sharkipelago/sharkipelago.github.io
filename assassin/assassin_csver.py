import csv
import datetime
import yaml

EVENT = "Event"
FAILED = "Failed"
WINNER = "Alexa"

eventlog = []
# Player Stats:
# 	Name:
# 	Pod:
# 	VictimNumber：
#   Assassin: 
# 	Kills: []
# 	DeathDate(Date of Death):
playerstats = {}
# Pod Stats:
# 	Members:
# 	Leathaliy：% of pod that got a kill
# 	KD(K/D): 
#   ExtinctionDate(Date of Extinction):
podstats = {}

# Returns true if d1, is later than d2
# If equal return false
def is_later(d1, d2):
    date1 = datetime.datetime.strptime(d1, "%b %d")
    date2 = datetime.datetime.strptime(d2, "%b %d")
    return date1 - date2  > datetime.timedelta(0) 

def readcsv(filename):
    with open(filename, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def set_eventlog():
    global eventlog
    eventlog = readcsv("eventlog.csv")

def get_players():
    return readcsv("players.csv")

def set_playerstats():  
    global playerstats

    if not eventlog:
        set_eventlog()

    playerstats = {p["Name"]:p for p in get_players()}
    kills = list(filter(lambda x: x["Event"] != EVENT and x["NewTarget"] != FAILED, eventlog))
    assert(len(kills) == len(playerstats) - 1)
    
    for p in playerstats.values(): p["Kills"] = []

    victim_number = 1       
    for kill in kills:
        assassin, victim = playerstats[kill["Assassin"]], playerstats[kill["Victim"]]
        # Assign Assassin
        victim["Assassin"] = assassin["Name"]
        # Assign Victim Number
        victim["VictimNumber"] = victim_number
        victim_number += 1
        # Increment Kills
        assassin["Kills"].append(victim["Name"])
        # Assign death date
        victim["DeathDate"] = kill["Date"]

def set_podstats():
    global podstats

    if not playerstats:
        set_playerstats()
    
    for player in playerstats.values():
        pod = player["Pod"]
        if pod not in podstats:
            podstats[pod] = {
                "Name": pod,
                "Members": [],
                "Leathality": 0,
                "KD": 0,
                "Extinction": ""
            }
        # Add members
        podstats[pod]["Members"].append(player["Name"])
    
    for pod in podstats.values():
        members = pod["Members"]
        leathality = 0
        kills = 0
        deaths = 0
        
        for name in members:
            player = playerstats[name]
            if player["Name"] != WINNER: 
                deaths += 1

            if len(player["Kills"]) == 0:
                continue
            leathality += 1
            kills += len(player["Kills"])

        pod["Leathality"] = str(int(round(leathality/len(members), 2) * 100)) + "%"
        pod["KD"] = round(kills/deaths, 2)

        if WINNER in members:
            del pod["Extinction"]
            continue

        latestDeath = "Jan 1"
        for name in members:
            player = playerstats[name]
            if (is_later(player["DeathDate"], latestDeath)):
                latestDeath = player["DeathDate"]
        pod["Extinction"] = latestDeath



def main():
    set_eventlog()
    set_playerstats()
    set_podstats()

    players = sorted(list(playerstats.values()), key=lambda x: x["VictimNumber"] if "VictimNumber" in x else 100)
    pods = list(podstats.values())  
    with open("players.yaml", "w") as playerFile:
        yaml.dump(players, playerFile)
    with open("pods.yaml", "w") as podFile:
        yaml.dump(pods, podFile)



if __name__ == "__main__":
    main()
