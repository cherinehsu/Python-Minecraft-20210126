from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
x,y,z = cherinehsu.player.getTilePos()

long = 10
big = 8
high = 7

block = 7
air = 0

cherinehsu.setBlocks(x,y,z,x+long,y+high,z+big,block)
cherinehsu.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,air)