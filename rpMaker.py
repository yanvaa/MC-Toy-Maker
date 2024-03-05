import ToyMaker
import requests
import mojang
import json
import os
import config
import uuids as uuidM

mojangAPI = mojang.API()
toyMaker = ToyMaker.STT()

def main(nicknames, download=True):
    for nickname, uuid, city, skin_type, url in nicknames:
        if download or not os.path.exists(f"skins/{nickname}.png"):
            with open(f"skins/{nickname}.png", "wb") as f:
                f.write(requests.get(url).content)
        toyMaker.make_toy(nickname, city, skin_type)
        print(nickname)
        
if __name__ == "__main__":
    data = []
    uuids = []
    
    uuidM.uuid()
    
    with open("uuid.json", "r") as f: uuids = json.loads(f.read())
    for uuid in uuids:
        data.append([uuid["nick"], uuid["uuid"], uuid["city"], uuid["skin_type"], uuid["skin_url"]])
    
    
    main(data, download=config.refresh)