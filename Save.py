def entry():

    gameRecord = open("game-entry", "w")
    gameRecord.write("Test1\n")
    gameRecord.write("Test2\n")
    gameRecord.write("Test3\n")
    gameRecord.close()


entry()
