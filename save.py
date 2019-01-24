def save_game(player_name, player_class, player_treasures):
    filehandle = open("SaveFile.txt", "a")
    player = [player_name, " ", player_class, " ", str(player_treasures), "\n"]
    filehandle.writelines(player)
    filehandle.close()



