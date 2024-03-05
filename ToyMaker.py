import pathlib
from os import mkdir
from os.path import exists

from PIL import Image

class STT:

    def __init__(self):
        if not exists("skins"):
            mkdir("skins")

        # resource pack dir creation
        if not exists("toys"):
            mkdir("toys")
        if not exists("toys\\pack.png"):
            image = Image.open("icon.png")
            image.save("toys\\pack.png")
        if not exists("toys\\pack.mcmeta"):
            with open("toys\\pack.mcmeta", "w+", encoding="utf-8") as prop_file:
                prop_file.write('{"pack":{"pack_format":13,"description":"§6Игрушки от §dYanva"}}')
        if not exists("toys\\assets"):
            mkdir("toys\\assets")
        if not exists("toys\\assets\\minecraft"):
            mkdir("toys\\assets\\minecraft")
        if not exists("toys\\assets\\minecraft\\optifine"):
            mkdir("toys\\assets\\minecraft\\optifine")
        if not exists("toys\\assets\\minecraft\\optifine\\cit"):
            mkdir("toys\\assets\\minecraft\\optifine\\cit")
        if not exists("toys\\assets\\minecraft\\optifine\\cit\\carved_pumpkin"):
            mkdir("toys\\assets\\minecraft\\optifine\\cit\\carved_pumpkin")

        self.directory = pathlib.Path("skins")
    
    def make_toy(self, user, city, skin_type, uol=True):
        dir_c = f"toys\\assets\\minecraft\\optifine\\cit\\carved_pumpkin\\" + city.lower().replace(" ", "_") + "\\"
        if "skins\\" not in str(user) and ".png" not in str(user):
            user = f"skins\{user}.png"
        nickname = str(user).split("\\")[1].removesuffix(".png")
        if not exists(dir_c): 
            mkdir(dir_c)
        dir_c += nickname.lower()  + "\\"
        if not exists(dir_c): 
            mkdir(dir_c)
        try:
            skin = Image.open(user).convert("RGBA")
            
            template_dir = "base.json"
            if skin_type == "slim":
                template_dir = "slimbase.json"
            
            skin.save(dir_c + nickname.lower() + ".png")
            with open(dir_c + f"{nickname.lower()}.properties",
                      "w+") as prop_file:
                prop_file.write(f"type=item\nmatchItems=minecraft:carved_pumpkin\n"
                                f"model=../../{template_dir}\ntexture={nickname.lower()}\nnbt.display.Name=ipattern:{nickname}")
        except FileNotFoundError:
            print(f"[Toy] Skin not found: [{nickname}]")