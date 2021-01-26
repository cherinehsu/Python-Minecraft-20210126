from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

import random
while True:
    x,y,z = cherinehsu.player.getTilePos()

    color = random.randrange(0,8)
    
    cherinehsu.setBlock(x,y,z+1,38,color)
    cherinehsu.setBlock(x,y,z-1,38,color)
    cherinehsu.setBlock(x-1,y,z,38,color)
    cherinehsu.setBlock(x+1,y,z,38,color)
    cherinehsu.setBlock(x+1,y,z+1,38,color)
    cherinehsu.setBlock(x-1,y,z+1,38,color)
    cherinehsu.setBlock(x-1,y,z-1,38,color)
    cherinehsu.setBlock(x+1,y,z-1,38,color)