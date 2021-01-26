from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

import random,time
while True:
    x,y,z = cherinehsu.player.getTilePos()

    color = random.randrange(0,16)
    cherinehsu.setBlocks(x+10,y,z+10,x-10,y,z-10,95,color)
    time.sleep(3)
