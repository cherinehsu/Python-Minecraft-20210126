from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
while True:
    x,y,z = cherinehsu.player.getTilePos()
    block1 = cherinehsu.getBlock(x,y-1,z)
    block2 = cherinehsu.getBlock(x+1,y-1,z)
    block3 = cherinehsu.getBlock(x-1,y-1,z)
    block4 = cherinehsu.getBlock(x,y-1,z+1)
    block5 = cherinehsu.getBlock(x,y-1,z-1)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9\
    or block3 == 8 or block3 == 9 or block4 == 8 or block4 == 9\
    or block5 == 8 or block5 == 9:
        cherinehsu.setBlock(x,y-1,z,138)
        cherinehsu.setBlock(x,y-1,z+1,138)
        cherinehsu.setBlock(x,y-1,z-1,138)
        cherinehsu.setBlock(x-1,y-1,z,138)
        cherinehsu.setBlock(x+1,y-1,z,138)