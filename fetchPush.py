
from requests import *
from deepdiff import DeepDiff
import os
import json
import time
from discordCon import send_update
#provide the api key
api_key = os.environ.get("HYPIXEL_API_KEY")


def errorHandler(data):
    curTime = time.time()
    curTime = time.ctime(curTime)

    if data == 400:
        print(f"( {curTime} )Error 400 : Some data is missing")

    elif data == 403:
        print(f"( {curTime} )Error 403 : Access Denied Invalid API Key")

    elif data == 422:
        print(f"( {curTime} )Error 422 : Data provided is invalid")

    elif data == 429:
        print(f"At ( {curTime} )  Error 429 : Request limit reached(u fucked up bro)")

def getPlayeruuid(username : str): #gets uuid from mojang
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = get(url)

    if response.status_code == 200:
        data = response.json()
        return data["id"]
    else:
        return None

uuid = getPlayeruuid("IHaveArms")

headerApi = {
    "API-Key" : api_key
}
params = {
    "uuid" : uuid
}


def addJson(data : dict = None ,header : str = None):

    if data is None:
        return print("no data")

    if header is None:
        return print("no header")

    defaultPath: list[str] = ["skyblock/", "resources/skyblock/"]
    path = f"{header}.json"

    fileJson = get(f"https://api.hypixel.net/v2/{defaultPath[data['id']]}{data['name']}", headers=headerApi,
                   params=params).json()
    if fileJson["success"] == False:
        return f"( {time.ctime(time.time())} ) ({header}) {fileJson['cause']}"

    if os.path.exists(path):

        with open(path,"r") as f:
            fileOrg = json.load(f)

        fileChanges = DeepDiff(fileOrg,
                               fileJson,
                               exclude_regex_paths=[r"lastUpdated",
                                                    r"buy_summary",
                                                    r"sell_summary",
                                                    r"quick_status"])

        if fileChanges == {}:
            return f"{time.ctime(time.time())} There are no differences for {header}"

        else:

            print(f"{time.ctime(time.time())} Differences have been found in {header} : \n {json.dumps(fileChanges.to_dict(),default = lambda x:list(x),indent=4)}")

            with open(path,"w")as f:
                json.dump(fileJson,fp = f, indent=4, sort_keys=True)

            send_update(header,fileChanges.to_json(indent = 4))

            return f"Successfully updated {header} pulled from {data['name']}"
    else:

        with open(path,"w") as f:
            json.dump(fileJson,fp = f, indent=4, sort_keys=True)

        return f"Successfully created {header} pulled from {data['name']}"

skyblockPicks = {# 0 is skyblock/ 1 is resources/skyblock
    "CollectionData": {"name": "collections", "id": 1},
    "SkillsData": {"name": "skills", "id": 1},
    "ItemsData": {"name": "items", "id": 1},
    "ElectionData": {"name": "election", "id": 1},
    "BingoData": {"name": "bingo", "id": 1},
    "NewsData": {"name": "news", "id": 0},
    #"AuctionData" : {"name": "auction", "id": 0},
    "BazaarData" : {"name": "bazaar", "id": 0},
    #"ProfilesData" : {"name" : "profiles", "id": 0} ,
    #"ProfileData": {"name": "profile", "id": 0},
}

for type in skyblockPicks:
    addJson(skyblockPicks[type], type)
    print(f"({time.ctime(time.time())}) Have finished processing : {type}")


def main():
    print("Starting Hypixel Tracker Service...")
    if not uuid:
        print("CRITICAL: Could not fetch Player UUID. Exiting.")
        return

    while True:
        print(f"\n--- Starting Cycle: {time.ctime(time.time())} ---")

        for type_key in skyblockPicks:
            result_msg = addJson(skyblockPicks[type_key], type_key)
            if result_msg:
                print(result_msg)

        print("Cycle complete. Sleeping for 10 minutes...")
        time.sleep(600)

if __name__ == "__main__":
    main()