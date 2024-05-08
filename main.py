from fotmanager import FotManager

m = FotManager("https://www.fotmob.com/api")

print(m.get_player_info("playerData",'30981'))
