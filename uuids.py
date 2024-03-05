from mojang import API
import json
import config

mojangAPI = API(retry_on_ratelimit=True)

def get_uuid(nick, city):
    uuid = mojangAPI.get_uuid(nick)
    profile = mojangAPI.get_profile(uuid)
    return {"uuid": uuid, "city": city, "nick": nick, "skin_type": profile.skin_variant, "skin_url": profile.skin_url}

def uuid():
    print(len(set(config.nicknames)))
    uuids = []
    for i in config.nicknames:
        uuids.append(get_uuid(i, "1"))
    print(uuids)
    with open("uuid.json", "w") as f:
        f.write(json.dumps(uuids))

if __name__ == "__main__": uuid()