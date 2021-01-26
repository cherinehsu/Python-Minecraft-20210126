from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

x,y,z = cherinehsu.player.getTilePos()
cherinehsu.setBlock(x,y,z+2,57)
cherinehsu.setBlock(x,y,z-2,57)
cherinehsu.setBlock(x-2,y,z,57)
cherinehsu.setBlock(x+2,y,z,57)
cherinehsu.setBlock(x+1,y,z+1,57)
cherinehsu.setBlock(x-1,y,z+1,57)
cherinehsu.setBlock(x+1,y,z-1,57)
cherinehsu.setBlock(x-1,y,z-1,57)