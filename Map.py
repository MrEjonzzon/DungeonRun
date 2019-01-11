mapcord = []

def mapsize(x, y):
    for r in range(x):
        for k in range(y):
            mapcord.append([r, k])
    print(mapcord)


diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
if diffpick == '1':
    mapsize(4, 4)
elif diffpick == '2':
    mapsize(5, 5)
elif diffpick == '3':
    mapsize(8, 8)

startroom = input('Were would you like to start?\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast')

direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S]To go south\n[D] to go east")
if
