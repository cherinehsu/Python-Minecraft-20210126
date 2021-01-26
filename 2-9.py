from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

x,y,z = cherinehsu.player.getTilePos()
cherinehsu.setSign(x,y,z+1,63,0,"我愛Minecraft","也愛Python")